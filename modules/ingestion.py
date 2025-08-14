from langchain.document_loaders import TextLoader

def load_documents(folder_path):
    # TODO: Add PDF, web, or other loaders if needed
    docs = []
    loader = TextLoader(f"{folder_path}/sample.txt")  # Start with one sample
    docs.extend(loader.load())
    return docs
