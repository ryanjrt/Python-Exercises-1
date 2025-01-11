import requests




city = input("Please enter your city of choice: ")#.strip()

#API endpoint
base_url = "http://api.weatherapi.com/v1"
selected_api = "/current.json"
api_key = "?key=e3b8fde100954d0ea0d165332251001"

api_call = base_url + selected_api + api_key + "&q=" + city
print(api_call)

response = requests.get(api_call)

#Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(f" City: {data['location']['name']}")
    print(f" Country: {data['location']['country']}")
    print(f" Temperature: {data['current']['temp_c']} C")
    print(f" Weather Conditions: {data['current']['condition']['text']}")
    print(f" Humidity: {data['current']['humidity']}")
    print(f" Last Updated: {data['current']['last_updated']}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")