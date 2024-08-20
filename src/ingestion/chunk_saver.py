import os

def save_chunks(chunks, save_dir="data/processed"):
    """
    Save text chunks along with their metadata to individual text files in the specified directory.

    Args:
    - chunks (List[Document]): List of Document chunks to save.
    - save_dir (str): Directory path to save the chunks. Defaults to "data/processed".
    """
    os.makedirs(save_dir, exist_ok=True)

    for i, chunk in enumerate(chunks):
        file_path = os.path.join(save_dir, f"chunk_{i + 1}.txt")
        
        with open(file_path, "w", encoding="utf-8") as f:
            for key, value in chunk.metadata.items():
                f.write(f"{key}: {value}\n")
            f.write(chunk.page_content)

    print(f"Saved {len(chunks)} chunks with metadata to {save_dir}.")
