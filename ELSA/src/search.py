def search_data(knowledge_base, query):
   ## Search for a query in the loaded knowledge base.
    
   ##  :param knowledge_base: List of dictionaries containing knowledge data.
    ## :param query: The search term.
    ## :return: A list of matched results.

    results = []
    
    for dataset in knowledge_base:
        for key, value in dataset.items():
            if query.lower() in key.lower() or query.lower() in str(value).lower():
                results.append({key: value})
    
    return results
