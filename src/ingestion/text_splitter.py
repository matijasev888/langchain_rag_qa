from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents, chunk_size=800, chunk_overlap=100):
    """
    Split the documents into smaller text chunks.

    Args:
    - documents: List of Document objects.
    - chunk_size: The size of each chunk in characters.
    - chunk_overlap: The number of characters to overlap between chunks.

    Returns:
    - chunks: List of Document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents)
    return chunks
