# ingestion.py

# Use the standard import compatible with LangChain 0.1.153
from langchain.document_loaders import TextLoader

def load_documents(folder_path):
    """
    Load documents from a folder.
    Currently supports plain text files. You can extend it to PDFs or web pages later.
    """
    docs = []
    loader = TextLoader(f"{folder_path}/sample.txt")  # Start with one sample
    docs.extend(loader.load())
    return docs
