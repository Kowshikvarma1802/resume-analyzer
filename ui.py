import streamlit as st
from pdf_parser import extract_text
from dotenv import load_dotenv
import os
import re
from groq import Groq
import tempfile


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text


def analyze(resume_text, job_desc):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze Resume vs Job Description and return:

1. ATS Score (0-100)
2. Matched Skills
3. Missing Skills
4. Resume Improvements
5. Interview Questions
6. Learning Roadmap

Resume:
{resume_text}

Job Description:
{job_desc}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload resume and paste job description")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_file and job_desc.strip():

        # Safe temp file handling
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        resume_text = clean_text(extract_text(temp_path))
        job_desc_clean = clean_text(job_desc)

        with st.spinner("Analyzing with AI..."):
            result = analyze(resume_text, job_desc_clean)

        st.success("Analysis Completed!")

        st.subheader("📊 AI Report")
        st.write(result)

    else:
        st.error("Please upload resume and job description")