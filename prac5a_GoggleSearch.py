#Search Website
import requests
import webbrowser

API_KEY = open("API_KEY").read().strip()
SEARCH_ENGINE_ID = open("SEARCH_ENGINE_ID").read().strip()

inp = input("Enter something for searching: ")
search_query = inp

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "q": search_query,
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)

if response.status_code == 200:
    results = response.json()
    if "items" in results and len(results["items"]) > 0:
        first_link = results["items"][0]["link"]
        print("Successfully found:", first_link)
        webbrowser.open(first_link)
    else:
        print("No results found")
elif response.status_code == 400:
    print("Bad Request Error (400):", response.json())
else:
    print("HTTP Error (Response status code):", response.status_code)
    print(response.text)

#Image
import requests

API_KEY = open("API_KEY").read()
SEARCH_ENGINE_ID = open("SEARCH_ENGINE_ID").read()

search_query = "car"

url = "https://www.googleapis.com/customsearch/v1"

params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'searchType': 'image'
}

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    print(item['link'])

API_KEY=AIzaSyBORUlQGEbvXY2cf2C2CNsHMltN6OL6Qpc
SEARCH_ENGINE_ID=834678b62e59a4602