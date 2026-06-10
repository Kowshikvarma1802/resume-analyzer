import streamlit as st

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume PDF")

if uploaded_file:
    st.success("File uploaded successfully")