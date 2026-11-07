# Note you need to run 'pip install requests' to use the request module 
import requests
people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print(json)

print("Number of people in space: ", json['number'])

for p in json['people']:
    print(p['name'])