# 🌍 Travel Ethiopia RAG Chatbot

Welcome to the Travel Ethiopia RAG Chatbot, an AI assistant that answers questions about Ethiopia using a Retrieval-Augmented Generation (RAG) system.

## 🚀 Project Overview

This project demonstrates a Naive RAG system:  

- Load custom documents (text files, PDFs, etc.).
- Generate embeddings using HuggingFace.
- Retrieve relevant information and generate answers.
- Interactive web interface via Streamlit.

  ## 🛠 Tech Stack

- **Python 3.12**  
- **[Streamlit](https://streamlit.io/)** – Web interface  
- **[LangChain](https://www.langchain.com/)** – RAG framework  
- **[FAISS](https://github.com/facebookresearch/faiss)** – Vector store  
- **[HuggingFace Embeddings](https://huggingface.co/)** – Free embeddings

  ## 📂 Project Structure


## ⚡ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/MikeCraftsStuff/travel-ethiopia-rag.git
cd travel-ethiopia-rag
pip install -r requirements.txt
streamlit run main.py


  ---

## **Step 6: Example Queries**
- Give users sample questions they can try.

```markdown
## 💡 Example Queries

- “What are the top tourist destinations in Ethiopia?”  
- “Tell me about Ethiopian traditional food.”  
- “Who was Emperor Haile Selassie?”

## ⚠️ Notes & Limitations

- Uses HuggingFace embeddings to avoid OpenAI API limits.  
- Best with small to medium document sets.  
- Currently supports text files; PDF or web scraping can be added.


## 🌐 Live Demo

*(Optional: Add your Streamlit Cloud or HuggingFace Spaces link here)*  

## 📜 License

MIT License – free to use and modify.

Built with curiosity, persistence, and a love for learning by **MikeCraftsStuff**
