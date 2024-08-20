import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.document_loader import load_documents
from src.ingestion.text_splitter import split_text
from src.ingestion.chunk_saver import save_chunks

def test_load_split_and_save_documents():
    # Step 1: Load the documents from test data
    documents = load_documents(data_path="data/test/raw")
    assert len(documents) > 0, "No documents loaded."
    print(f"Loaded {len(documents)} documents.")

    # Step 2: Split the documents into chunks
    chunks = split_text(documents)
    assert len(chunks) > 0, "No chunks created from documents."
    print(f"Split documents into {len(chunks)} chunks.")
    print("Exemple of a chunk: ")
    print()
    print(chunks[0])
    print()

    # Step 3: Save the chunks to the test processed directory
    save_chunks(chunks, save_dir="data/test/processed")
    print("Chunks saved successfully to test processed directory.")

if __name__ == "__main__":
    test_load_split_and_save_documents()
