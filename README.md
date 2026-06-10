# Resume Analyzer (AI Powered ATS System)

## Overview
An AI-powered Resume Analyzer that extracts and evaluates resumes against job descriptions using Natural Language Processing (NLP).
It generates an ATS (Applicant Tracking System) score to help candidates understand their job match quality and improve their resume.

---

## Key Features
- Extracts structured text from PDF resumes
- Text preprocessing (cleaning, tokenization, stopword removal)
- Keyword matching with job descriptions
- ATS compatibility score generation
- Vector-based similarity matching
- Fast analysis pipeline

---

## Tech Stack
- Python
- NLP (NLTK / spaCy)
- Scikit-learn (TF-IDF / similarity)
- PDF parsing libraries (PyPDF2 / pdfminer)
- Vector-based text similarity methods

---

## System Architecture
Resume (PDF)
→ Text Extraction (pdf_parser.py)
→ Text Preprocessing
→ Vectorization (vector_store.py)
→ Matching with Job Description
→ ATS Score Generation

---

## Project Structure
- app.py → Core application logic
- ui.py → User interface layer
- pdf_parser.py → PDF text extraction module
- vector_store.py → Vector similarity computation
- requirements.txt → Project dependencies

---

## How to Run
```bash
pip install -r requirements.txt
python app.py
