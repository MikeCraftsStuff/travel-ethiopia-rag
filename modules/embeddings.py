from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_embeddings(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
