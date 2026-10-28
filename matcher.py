"""Skill extraction and practical recommendations for Smart Resume Matcher."""

import re

# Canonical skill names are returned by find_skills().
SKILL_ALIASES = {
    "python": ["python", "python programming"],
    "sql": ["sql", "structured query language"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "machine learning": ["machine learning", "ml"],
    "scikit-learn": ["scikit-learn", "scikit learn", "sklearn"],
    "deep learning": ["deep learning"],
    "natural language processing": ["natural language processing", "nlp"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch", "torch"],
    "statistics": ["statistics", "statistical analysis"],
    "data analysis": ["data analysis", "data analytics", "analyzing data", "analysing data"],
    "data visualization": ["data visualization", "data visualisation", "data viz"],
    "data cleaning": ["data cleaning", "data cleansing", "data preprocessing", "data wrangling"],
    "excel": ["excel", "microsoft excel", "ms excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "java": ["java"],
    "javascript": ["javascript", "java script", "js"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "react": ["react", "react.js", "reactjs"],
    "flask": ["flask"],
    "fastapi": ["fastapi", "fast api"],
    "streamlit": ["streamlit"],
    "rest api": ["rest api", "rest apis", "restful api", "restful apis"],
    "git": ["git", "version control"],
    "github": ["github"],
    "docker": ["docker", "containerization", "containerisation"],
    "linux": ["linux"],
    "aws": ["aws", "amazon web services"],
    "cloud computing": ["cloud computing"],
    "postgresql": ["postgresql", "postgres"],
    "mysql": ["mysql"],
    "mongodb": ["mongodb", "mongo db"],
    "etl": ["etl", "extract transform load"],
    "data engineering": ["data engineering", "data pipelines"],
    "communication": ["communication", "communication skills", "verbal communication"],
    "teamwork": ["teamwork", "team work", "collaboration"],
    "problem solving": ["problem solving", "problem-solving", "analytical thinking"],
    "project management": ["project management"],
}

SKILLS = list(SKILL_ALIASES)

recommendations = {
    "python": "Practise Python fundamentals, functions, file handling, and build a small application.",
    "sql": "Practise SELECT, WHERE, JOIN, GROUP BY, subqueries, and window functions.",
    "pandas": "Clean, filter, group, and analyze a real CSV dataset with pandas.",
    "numpy": "Practise arrays, indexing, vectorized operations, and aggregations.",
    "machine learning": "Learn train/test splits, baseline models, evaluation metrics, and model limitations.",
    "scikit-learn": "Build a small classification or regression pipeline and evaluate it on held-out data.",
    "deep learning": "Learn neural-network basics and when deep learning is appropriate compared with simpler models.",
    "natural language processing": "Practise text cleaning, tokenization, TF-IDF, and text classification.",
    "tensorflow": "Follow a small end-to-end TensorFlow example and evaluate it on test data.",
    "pytorch": "Build a small model in PyTorch and practise tensors, training loops, and evaluation.",
    "statistics": "Review distributions, averages, variance, correlation, and sampling.",
    "data analysis": "Choose a real dataset, answer clear questions, and explain findings with evidence.",
    "data visualization": "Choose charts that match the question and label axes and units clearly.",
    "data cleaning": "Practise handling missing values, duplicates, inconsistent categories, and invalid data types.",
    "excel": "Practise formulas, lookup functions, sorting, filtering, and pivot tables.",
    "power bi": "Build a dashboard with a clear data model, measures, filters, and readable visuals.",
    "tableau": "Create a dashboard from a sample dataset and explain the main insights.",
    "matplotlib": "Build clear, labelled charts and practise choosing appropriate chart types.",
    "seaborn": "Practise statistical charts and readable visual summaries.",
    "java": "Practise object-oriented programming, collections, exceptions, and small console projects.",
    "javascript": "Build interactive web-page features and practise functions, arrays, objects, and async basics.",
    "html": "Practise semantic page structure, accessible forms, and meaningful headings.",
    "css": "Practise responsive layouts, Flexbox/Grid, spacing, and accessible contrast.",
    "react": "Build a small component-based interface and practise state and props.",
    "flask": "Build a small web API with routes, input validation, and error handling.",
    "fastapi": "Build and test a small API with request validation and clear response models.",
    "streamlit": "Improve the app with clear layout, helpful errors, and a complete user workflow.",
    "rest api": "Practise HTTP methods, status codes, JSON payloads, and API error handling.",
    "git": "Practise meaningful commits, branches, .gitignore, and resolving simple merge conflicts.",
    "github": "Write a clear README, add screenshots, and document setup and known limitations.",
    "docker": "Containerize a small app and document how to build and run the image.",
    "linux": "Practise shell navigation, files, permissions, processes, and environment variables.",
    "aws": "Learn core cloud concepts and deploy a small project using free-tier resources where eligible.",
    "cloud computing": "Learn deployment basics, storage, networking, permissions, and cost controls.",
    "postgresql": "Practise table design, joins, constraints, indexes, and transactions.",
    "mysql": "Practise relational table design, joins, constraints, and query optimization basics.",
    "mongodb": "Learn document modelling, CRUD operations, indexes, and when a document database fits.",
    "etl": "Build a simple extract-transform-load pipeline with validation and logging.",
    "data engineering": "Build a repeatable data pipeline with validation, clear outputs, and error handling.",
    "communication": "Practise explaining a project, your decisions, and results in concise, concrete language.",
    "teamwork": "Prepare examples of collaboration, feedback, conflict resolution, and shared delivery.",
    "problem solving": "Explain your approach step by step and compare alternatives using evidence.",
    "project management": "Practise defining scope, milestones, risks, and measurable acceptance criteria.",
}


def find_skills(text):
    """Return recognized canonical skills found as whole terms in text."""
    if not isinstance(text, str) or not text.strip():
        return []

    normalized = text.lower()
    found = []
    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            pattern = r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"
            if re.search(pattern, normalized):
                found.append(skill)
                break
    return found
