from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def retrieve_relevant_chunks(query, faiss_index_path="data/embeddings/faiss_index"):
    """
    Retrieve relevant chunks from the FAISS index based on the user's query.

    Args:
    - query (str): The user's query to search for relevant chunks.
    - faiss_index_path (str): Path to the FAISS index. Defaults to "data/embeddings/faiss_index".

    Returns:
    - relevant_chunks (List[Tuple[Document, float]]): List of tuples containing Document objects
      that are relevant to the query along with their similarity scores.
    """
    embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    vector_store = FAISS.load_local(faiss_index_path, embeddings_model, allow_dangerous_deserialization=True)
    
    relevant_chunks = vector_store.similarity_search_with_score(query)
    
    return relevant_chunks
