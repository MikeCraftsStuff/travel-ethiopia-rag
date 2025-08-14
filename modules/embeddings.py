
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_embeddings(documents):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
