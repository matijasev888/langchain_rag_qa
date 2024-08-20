from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents(data_path="data/raw"):
    """
    Load PDF documents from the specified directory.

    Args:
    - data_path (str): Directory path for PDF files. Defaults to "data/raw".

    Returns:
    - documents (List[Document]): List of Document objects with extracted text.
    """
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()

    return documents
