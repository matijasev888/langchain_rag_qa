import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv 
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))


from flask import Flask, request, jsonify, render_template
from src.retrieval.retriever import retrieve_relevant_chunks
from src.generation.answer_generator import generate_answer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-answer', methods=['POST'])
def generate_answer_endpoint():
    data = request.json
    query = data.get('query')
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    try:
        retrieved_documents = retrieve_relevant_chunks(query, faiss_index_path="data/embeddings/faiss_index")
        answer, document_info = generate_answer(query, retrieved_documents)
        return jsonify({"query": query, "answer": answer, "document_info": document_info})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
