from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def store_embeddings(documents, path="data/embeddings/faiss_index"):
    """
    Store the embeddings in a FAISS index using HuggingFace embeddings.

    Args:
    - documents (List[Document]): List of Document objects to generate embeddings for.
    - path (str): Directory path to save the FAISS index. Defaults to "data/embeddings/faiss_index".
    """
    embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings_model)
    vector_store.save_local(path)
    
    return vector_store
