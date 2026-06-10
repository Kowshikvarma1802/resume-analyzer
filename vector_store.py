from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -----------------------------
# 1. SPLIT TEXT INTO CHUNKS
# -----------------------------
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(text)

# -----------------------------
# 2. CREATE VECTOR STORE
# -----------------------------
def create_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_store = FAISS.from_texts(
        text_chunks,
        embedding=embeddings
    )

    return vector_store

# -----------------------------
# 3. RETRIEVE RELEVANT CHUNKS
# -----------------------------
def retrieve_relevant_chunks(vector_store, query, k=4):
    docs = vector_store.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]