
import streamlit as st



st.set_page_config(
    page_title="Smart Resume Matcher",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Smart Resume Matcher")
st.write(
    "Compare a resume with a job description, identify matching skills, "
    "and discover areas to improve."
)
st.caption(
    "The similarity score compares text; it is not a hiring probability "
    "or a guarantee of job fit."
)


from core import analyze, csv_report, extract_text, pdf_report, txt_report

with st.sidebar:
    st.header("Upload files")
    resume_file = st.file_uploader(
        "Resume", type=["pdf", "docx", "txt"], key="resume_upload"
    )
    job_file = st.file_uploader(
        "Job description", type=["pdf", "docx", "txt"], key="job_upload"
    )
    st.caption(
        "Supported formats: PDF, DOCX, and TXT. Scanned image-only PDFs "
        "may not contain extractable text."
    )

uploaded_resume_text = ""
uploaded_job_text = ""

if resume_file is not None:
    try:
        uploaded_resume_text = extract_text(resume_file)
    except Exception as exc:
        st.error(f"Could not read resume file: {exc}")

if job_file is not None:
    try:
        uploaded_job_text = extract_text(job_file)
    except Exception as exc:
        st.error(f"Could not read job description file: {exc}")

left, right = st.columns(2)

with left:
    st.subheader("Resume text")
    if resume_file is not None and uploaded_resume_text:
        st.caption(
            f"File loaded: {resume_file.name}. Paste text below only "
            "if you want to override the uploaded file."
        )
    resume_manual = st.text_area(
        "Paste or type resume text",
        height=250,
        key="resume_manual_input",
        placeholder="Paste your resume here, or upload a file in the sidebar.",
    )

with right:
    st.subheader("Job description text")
    if job_file is not None and uploaded_job_text:
        st.caption(
            f"File loaded: {job_file.name}. Paste text below only "
            "if you want to override the uploaded file."
        )
    job_manual = st.text_area(
        "Paste or type job description",
        height=250,
        key="job_manual_input",
        placeholder="Paste the job description here, or upload a file in the sidebar.",
    )

resume_text = resume_manual.strip() or uploaded_resume_text.strip()
job_text = job_manual.strip() or uploaded_job_text.strip()
resume_name = (
    "Pasted resume text"
    if resume_manual.strip()
    else resume_file.name if resume_file else "Pasted resume text"
)
job_name = (
    "Pasted job description text"
    if job_manual.strip()
    else job_file.name if job_file else "Pasted job description text"
)

if st.button("Analyze Resume", type="primary", use_container_width=True):
    if not resume_text:
        st.error("Upload a resume or paste resume text before analyzing.")
    elif not job_text:
        st.error("Upload a job description or paste its text before analyzing.")
    else:
        try:
            st.session_state["analysis_result"] = analyze(
                resume_text, job_text, resume_name, job_name
            )
        except Exception as exc:
            st.session_state.pop("analysis_result", None)
            st.error(f"Analysis failed: {exc}")

result = st.session_state.get("analysis_result")

if result:
    st.divider()
    st.header("Analysis results")
    st.metric("Resume-to-job text similarity", f"{result['score']}%")
    st.caption(
        "This percentage measures text similarity, not the probability "
        "of getting hired."
    )

    col1, col2 = st.columns(2)
    col1.metric("Matched skills", len(result["matched"]))
    col2.metric("Skills to improve", len(result["missing"]))

    st.subheader("Matched skills")
    if result["matched"]:
        st.write(", ".join(result["matched"]))
    else:
        st.info("No matching skills were detected by the current skill list.")

    st.subheader("Skills to improve")
    if result["missing"]:
        st.write(", ".join(result["missing"]))
    else:
        st.success("No missing skills were detected by the current skill list.")

    st.subheader("Recommendations")
    if result["recommendations"]:
        for item in result["recommendations"]:
            st.write(f"- {item}")
    elif result["missing"]:
        st.info("No recommendations were generated for these missing skills.")
    else:
        st.success("Your detected skills match the detected job skills.")

    with st.expander("View detected skills"):
        st.write("**Skills detected in resume**")
        st.write(", ".join(result["resume_skills"]) or "None detected")
        st.write("**Skills detected in job description**")
        st.write(", ".join(result["job_skills"]) or "None detected")

    st.divider()
    st.subheader("Download report")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            "Download TXT",
            data=txt_report(result),
            file_name="resume_match_report.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with col2:
        st.download_button(
            "Download CSV",
            data=csv_report(result),
            file_name="resume_match_report.csv",
            mime="text/csv",
            use_container_width=True,
        )
    with col3:
        try:
            pdf_data = pdf_report(result)
            st.download_button(
                "Download PDF",
                data=pdf_data,
                file_name="resume_match_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        except ImportError:
            st.warning(
                "PDF reports require reportlab. Install it with: pip install reportlab"
            )
else:
    st.info("Upload both files or paste both texts, then click Analyze Resume.")
