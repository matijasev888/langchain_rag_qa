import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.retrieval.retriever import retrieve_relevant_chunks

def test_retrieve_relevant_chunks():
    query = "What is Hotel?"

    # Call the function to retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(query, faiss_index_path="data/test/embeddings/faiss_index")
    
    print(f"Query: {query}")
    for i, (doc, score) in enumerate(relevant_chunks):
        print()
        print(f"Document {i+1}: {doc.page_content[:100]}... (Score: {score})")
        

    # Simple assertion to check if we got results
    assert len(relevant_chunks) > 0, "No relevant chunks were retrieved."

if __name__ == "__main__":
    test_retrieve_relevant_chunks()
