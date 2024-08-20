import os
from langchain.schema import Document

def load_chunks(processed_dir="data/processed"):
    """
    Load text chunks from the processed directory and convert them into Document objects.

    Args:
    - processed_dir (str): Directory path where the processed chunks are stored. 
                           Defaults to "data/processed".

    Returns:
    - chunks (List[Document]): List of Document objects created from the text chunks.
    """
    chunks = []
    for filename in sorted(os.listdir(processed_dir)):
        file_path = os.path.join(processed_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            chunks.append(Document(page_content=content))
    return chunks
