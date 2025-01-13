import requests

#Construct API call
def get_api_call(city):
    base_url = "http://api.weatherapi.com/v1"
    selected_api = "/current.json"
    api_key = "?key=e3b8fde100954d0ea0d165332251001"
    
    call = base_url + selected_api + api_key + "&q=" + city  
    print(call) #DEBUG
    return call

#Get the weather conditions from API call
def get_weather(call):
    response = requests.get(call)
    #Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

#Main program
def main():
    print("Welcome to Weatherman.io!")
    
    #Prompt user for cities input
    cities = input("Please enter your cities of choice (separated by commas ','): ").split(",")
    #print(f"before strip: {cities}") #DEBUG
    cities = [city.strip() for city in cities if city.strip()]
    #print(cities) #DEBUG
    
    #Construct API call
    api_call = []
    for city in cities:
        api_call.append(get_api_call(city))
    
    #Get weather conditions    
    for call in api_call:
        data = get_weather(call)
        location = data['location']['name']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        weather = data['current']['condition']['text']
        humidity = data['current']['humidity']
        updated = data['current']['last_updated']
        print(f"Weather conditions for: {location}, {country}:")
        print(f"    Temperature: {temperature} C:")      
        print(f"    Weather: {weather}:")      
        print(f"    Humidity: {humidity}:")        
        print(f"    Last updated: {updated}/n:")

if __name__ == "__main__":
    main()
    