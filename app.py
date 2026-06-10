from vector_store import split_text, create_vector_store, retrieve_relevant_chunks

def analyze_resume(resume_text, job_desc):

    # STEP 1: Chunk resume
    chunks = split_text(resume_text)

    # STEP 2: Create FAISS DB
    vector_store = create_vector_store(chunks)

    # STEP 3: Retrieve relevant chunks based on JD
    relevant_chunks = retrieve_relevant_chunks(vector_store, job_desc)

    # STEP 4: Combine only relevant info
    context = "\n".join(relevant_chunks)

    prompt = f"""
You are an expert ATS Resume Analyzer using RAG.

Analyze Resume vs Job Description.

Use ONLY the provided resume context.

Resume Context:
{context}

Job Description:
{job_desc}

Return:
1. ATS Score (0-100)
2. Matched Skills
3. Missing Skills
4. Resume Improvements
5. Interview Questions
6. Learning Roadmap
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content