# modules/ingestion.py
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(folder_path):
    """Load and split all text files from the given folder."""
    documents = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Only load .txt files
        if file_name.lower().endswith(".txt"):
            loader = TextLoader(file_path, encoding='utf-8')
            docs = loader.load()
            documents.extend(docs)
    
    if not documents:
        raise ValueError("No text files found in documents/ folder.")
    
    # Split long docs into smaller chunks for better retrieval
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)
    return split_docs
