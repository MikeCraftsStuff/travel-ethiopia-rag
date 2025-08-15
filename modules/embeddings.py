# modules/embeddings.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embeddings(documents):
    """Generate embeddings and store them in a FAISS vector store."""
    # Using free sentence-transformers model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create vector store
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
