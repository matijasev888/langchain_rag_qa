import warnings
warnings.filterwarnings("ignore", message="`clean_up_tokenization_spaces` was not set")

from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'config', '.env'))

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.retrieval.retriever import retrieve_relevant_chunks
from src.generation.answer_generator import generate_answer

def test_retrieval_and_generation():
    query = "What is Hotel?"

    # Retrieve relevant chunks
    retrieved_documents = retrieve_relevant_chunks(query, faiss_index_path="data/test/embeddings/faiss_index")
    
    # Generate the answer using the retrieved documents
    answer, document_info = generate_answer(query, retrieved_documents)
    
    print(f"\nQuery: {query}")
    print(f"\nAnswer:{answer}")
    print(f"\nSources:\n{document_info}")

if __name__ == "__main__":
    test_retrieval_and_generation()
