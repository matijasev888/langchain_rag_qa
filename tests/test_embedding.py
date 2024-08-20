import warnings
warnings.filterwarnings("ignore", message="`clean_up_tokenization_spaces` was not set")

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.chunk_loader import load_chunks
from src.embedding.vector_store import store_embeddings

def test_load_chunks_and_store_embeddings():
    # Step 1: Load the chunks from the test processed directory
    documents = load_chunks(processed_dir="data/test/processed")
    assert len(documents) > 0, "No chunks loaded from processed data."
    print(f"Loaded {len(documents)} chunks from test processed data.")

    # Step 2: Store embeddings in the test FAISS directory
    test_faiss_path = "data/test/embeddings/faiss_index"
    store_embeddings(documents, path=test_faiss_path)
    print(f"Embeddings stored in FAISS index at {test_faiss_path}.")

if __name__ == "__main__":
    test_load_chunks_and_store_embeddings()
