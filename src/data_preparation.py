import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.document_loader import load_documents
from src.ingestion.text_splitter import split_text
from src.ingestion.chunk_saver import save_chunks
from src.ingestion.chunk_loader import load_chunks
from src.embedding.vector_store import store_embeddings

def prepare_data():

    # Step 1: Load raw documents
    print("Loading documents...")
    documents = load_documents(data_path="data/raw")

    # Step 2: Split documents into chunks
    print("Splitting documents into chunks...")
    chunks = split_text(documents)

    # Step 3: Save the chunks to the test processed directory
    print("Storing chunks...")
    save_chunks(chunks, save_dir="data/processed")
    
    # Step 4: Load documents
    documents = load_chunks(processed_dir="data/processed")

    # Step 5: Store embeddings in FAISS
    print("Storing embeddings in FAISS index...")
    store_embeddings(documents, path="data/embeddings/faiss_index")

    print("Data preparation complete.")

if __name__ == "__main__":
    prepare_data()
