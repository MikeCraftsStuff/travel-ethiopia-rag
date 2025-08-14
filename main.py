from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

from flask import Flask, render_template, request
from modules.ingestion import load_documents
from modules.embeddings import create_embeddings
from modules.retrieval import retrieve_relevant_chunks
from modules.generator import generate_answer

app = Flask(__name__)

# Load and index documents at startup
documents = load_documents("documents/")
embeddings_index = create_embeddings(documents)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        query = request.form.get("query")
        relevant_chunks = retrieve_relevant_chunks(query, embeddings_index)
        answer = generate_answer(query, relevant_chunks)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)



print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))