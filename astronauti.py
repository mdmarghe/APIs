import json
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

file = open("iss.txt", "w")
file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")

for person in result["people"]:
    file.write(person['name'] + " - onboard\n")

file.close()

import geocoder

g = geocoder.ip('me')
print(f"Your current location: {g.latlng}")