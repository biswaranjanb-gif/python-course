# Weather API (https://www.weatherapi.com/) - Get weather information based on user input city
import requests

city = input("Enter your city name: ")
url = "http://api.weatherapi.com/v1/current.json?key=ae07cbdcb18a4d80931111343261210&q=" + city + "&aqi=no"

response = requests.get(url)
weather_json = response.json()

country = weather_json['location']['country']
temperature = weather_json['current']['temp_f']

print("Weather of " + city + " located in " + country + " is: " + str(temperature) + "°F")
