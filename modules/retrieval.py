def retrieve_relevant_chunks(query, vector_store, k=3):
    # Retrieve top-k relevant chunks
    results = vector_store.similarity_search(query, k=k)
    return results
