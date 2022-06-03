import requests
import json
import firebase_admin
import schedule

params_3060 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3060',
    'sort_by': 'price_low_to_high'
}

params_3070 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3070',
    'sort_by': 'price_low_to_high'
}

params_3080 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3080',
    'sort_by': 'price_low_to_high'
}

def fetch_data_product(params):
    # MAKE API CALL
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    api_response = json.loads(api_result.text)

    # EXTRACT SEARCH RESULT DATA
    search_results = api_response['search_results']

    # EXCLUDE UNWANTED SEARCH RESULT DATA
    search_results_refined = []

    for x in range(0, 10):
        search_results_refined.append(search_results[x])

    # FORMAT DATA
    filtered_search_results = []

    for search in search_results_refined:
        name = search["title"]

        try:
            price = search["price"]["value"]
        except:
            price = "No Price Listed"

        image = search["image"]
        link = search["link"]

        formatted_json = {
            "name" : name,
            "price" : price,
            "image" : image,
            "link" : link
        }

        filtered_search_results.append(formatted_json)

    return filtered_search_results

def upload_data():
    data_3060 = fetch_data_product(params_3060)
    data_3070 = fetch_data_product(params_3070)
    data_3080 = fetch_data_product(params_3080)


def main():
    api_response = fetch_data_product(params_3070)
    print(json.dumps(api_response))

main()
#schedule.every(10).minutes.do(upload_data())



