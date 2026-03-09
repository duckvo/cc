import requests

def get_geolocation(api_key, search_string):
    base_url = "https://us1.locationiq.com/v1/search.php"
    params = {
        'key': api_key,
        'q': search_string,
        'format': 'json'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()   # raises error for 4xx / 5xx

        data = response.json()

        if data:
            return {
                'place_id': data[0].get('place_id', ''),
                'lat': data[0].get('lat', ''),
                'lon': data[0].get('lon', ''),
                'display_name': data[0].get('display_name', '')
            }
        else:
            print("Error: Empty response from API")
            return None

    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return None


api_key = 'pk.656865accc1639dc4785ef5185a39f50'
search_string = input("Enter the location: ")

result = get_geolocation(api_key, search_string)

if result:
    print("Output:")
    for key, value in result.items():
        print(f"{key}: {value}")
