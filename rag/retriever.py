from rag.vectordb import collection

def retrieve_company_info(company):

    result = collection.query(
        query_texts=[company],
        n_results=1
    )

    return result["documents"][0][0]