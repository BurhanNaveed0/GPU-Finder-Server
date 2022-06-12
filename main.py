import requests
import json
import pyrebase
import schedule

# SEARCH PARAMETERS
params_3060 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3060',
    'exclude_sponsored': "true",
    'max_page' : '5',
    'sort_by': 'price_low_to_high'
}

params_3070 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3070',
    'exclude_sponsored': "true",
    'max_page' : '5',
    'sort_by': 'price_low_to_high'
}

params_3080 = {
    'api_key': '78C3B9733F7840B7B25DDE8CC464A3D7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'RTX 3080',
    'exclude_sponsored': "true",
    'refinements' : "p_36/2421890011",
    'max_page' : '5',
    'sort_by': 'price_low_to_high'
}

# DATABASE CONFIGURATION
config = {
  "apiKey": "AIzaSyADEPTyHHzEXAgSdW0kMC7EyHTlV1rS_b8",
  "authDomain": "gpu-finder-database.firebaseapp.com",
  "databaseURL": "https://gpu-finder-database-default-rtdb.firebaseio.com",
  "projectId": "gpu-finder-database",
  "storageBucket": "gpu-finder-database.appspot.com",
  "messagingSenderId": "85929553382",
  "appId": "1:85929553382:web:1236442a8e7798bd997a27",
  "measurementId": "G-MN1138YJLV"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

def get_msrp(name):
    if(name == '3060'):
        return 329
    elif(name == '3070'):
        return 499
    elif(name == '3080'):
        return 780

def fetch_data_product(params):
    # MAKE API CALL
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    api_response = json.loads(api_result.text)

    # EXTRACT SEARCH RESULT DATA
    search_results = api_response['search_results']

    # EXCLUDE UNWANTED SEARCH RESULT DATA
    search_results_refined = []
    index = 0
    name = params["search_term"][-4:]

    while(len(search_results_refined) < 10 and index < len(search_results)):
        try:
            if(name in search_results[index]["title"] and int(search_results[index]["price"]["value"]) >= get_msrp(name)):
                search_results_refined.append(search_results[index])
        except:
            pass
        
        index += 1

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
    # FETCH PRODUCT DATA
    data_3060 = fetch_data_product(params_3060)
    data_3070 = fetch_data_product(params_3070)
    data_3080 = fetch_data_product(params_3080)

    # PUSH SEARCH DATA
    database.child("3060").set(data_3060)
    database.child("3070").set(data_3070)
    database.child("3080").set(data_3080)

#schedule.every(5).minutes.do(upload_data())

upload_data()






