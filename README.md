# Smart Resume Matcher

A local Streamlit app that compares resume text with a job description, detects skills from the skill dictionary, suggests learning steps for missing skills, and exports TXT, CSV, and PDF reports.

## Start on Windows

1. Extract this folder.
2. Double-click `START_APP.bat`.
3. Wait for Streamlit to start. Your browser should open automatically. If it does not, open the local URL printed in the terminal (usually `http://localhost:8501`).

The first run installs packages from `requirements.txt`, so an internet connection is required for setup.

## Manual start

Open a terminal in this folder and run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Features

- Paste resume and job-description text or upload PDF, DOCX, and TXT files.
- Detect skills and aliases defined in `matcher.py`.
- Show matched and missing skills, with recommendations for detected missing skills.
- Calculate a TF-IDF text-similarity percentage.
- Download TXT, CSV, and PDF reports.

## Important limitations

- The percentage is text similarity, not a hiring probability or a guarantee of job fit.
- Skill detection only recognizes terms and aliases listed in `matcher.py`.
- Scanned image-only PDFs need OCR, which is not included.
- This is a local rule-based/text-similarity tool, not a generative AI model.
