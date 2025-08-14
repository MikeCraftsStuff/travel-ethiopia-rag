# main.py
import streamlit as st
from modules.ingestion import load_documents
from modules.embeddings import create_embeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

# --- Load Documents ---
st.title("Travel Ethiopia RAG Chatbot")
st.write("Ask questions about Ethiopia!")

# Make sure your documents are in the 'documents/' folder
documents = load_documents("documents/")

# --- Create Embeddings and Vector Store ---
vector_store = create_embeddings(documents)

# --- Setup Retriever ---
retriever = vector_store.as_retriever(search_kwargs={"k": 3})  # return top 3 relevant chunks

# --- Setup LLM ---
# Using HuggingFace model (local/free)
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",  # you can switch to any model you like
    model_kwargs={"temperature": 0}
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# --- Streamlit User Interface ---
user_question = st.text_input("Your Question:")

if user_question:
    response = qa_chain.run(user_question)
    st.write("**Answer:**")
    st.write(response)
