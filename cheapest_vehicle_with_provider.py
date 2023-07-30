def find_cheapest_from_provider(results: list) -> str:
    """
    Finds the cheapest result ID from a list of results provided by different providers.

    This function filters the given list of results to only include those from the provider named
    'Dummy External Provider'. Then, it identifies the result with the minimum total price among
    these filtered results and returns its result ID.

    :param results: A list of dictionaries representing different results, where each result
                    must have a 'steps' key containing a list of steps, and each step must
                    have a 'details' key containing a dictionary with 'provider_name' as the
                    name of the provider and 'total_price' as the total price information.

    :return: result_id: The result ID of the cheapest result from the 'Dummy External Provider'.
    """

    new_list = list()
    for result in results:
        if result['steps'][0]['details']['provider_name'] == 'Dummy External Provider':
            new_list.append(result)
    min_price_result = min(new_list, key=lambda x: float(x["total_price"]['total_price']['value']))
    return min_price_result.get('result_id')
