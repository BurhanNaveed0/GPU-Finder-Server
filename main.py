import requests
import json

params_3060 = {
  'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
  'type': 'search',
  'amazon_domain': 'amazon.com',
  'search_term': 'RTX 3060',
  'sort_by': ''
}

params_3070 = {
  'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
  'type': 'search',
  'amazon_domain': 'amazon.com',
  'search_term': 'RTX 3070',
  'sort_by': 'price_high_to_low'
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

    # REFINE SEARCH RESULT DATA
    search_results_refined = []

    for x in range(0, 10):
      search_results_refined.append(search_results[x])

    # FORMAT DATA
    for search in search_results_refined:
      name = search["title"]
      link = search["link"]
      
    return search_results_refined

def upload_data():
    print('hello')

def main():
    api_response = fetch_data_product(params_3070)
    print(json.dumps(api_response))

main()



