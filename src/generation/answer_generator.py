from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import HuggingFaceHub

def generate_answer(query, retrieved_documents):
    """
    Generate an answer to the user's query based on pre-retrieved documents.

    Args:
    - query (str): The user's query.
    - retrieved_documents (List[Tuple[Document, float]]): List of tuples containing Document objects
      that are relevant to the query along with their similarity scores.

    Returns:
    - answer (str): The generated answer to the query, along with the source document information.
    """
    llm = HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
    
    qa_chain = load_qa_chain(llm, chain_type="stuff")
    
    docs = [doc[0] for doc in retrieved_documents]
    result = qa_chain.invoke({"input_documents": docs, "question": query})
    
    answer = result['output_text'].split('Helpful Answer:')[-1].strip()
    document_info = "\n".join([f"Document {i+1}: {doc.page_content}\n" for i, (doc, score) in enumerate(retrieved_documents)])
    
    return (answer, document_info)