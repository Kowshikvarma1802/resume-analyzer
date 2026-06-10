import streamlit as st

st.set_page_config(page_title="Resume Analyzer")

st.title("Resume Analyzer")

st.write("Upload your resume PDF and analyze ATS score")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")
    st.write("App is working correctly 🎉")