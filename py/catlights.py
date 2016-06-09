import json
import requests

config = json.loads(open('config.json', 'r').read())

url = 'http://' + config['hue']['bridgeaddress']  + '/api/' + config['hue']['bridgeusername'] + '/lights/'
response = requests.get(url)

lightsJSON = response.json()

# Show on lights
print("these lights are on")
for light in lightsJSON:
  if lightsJSON[light]['state']['on'] == True:
    print (light, '=', lightsJSON[light]['name'])
  
print("these lights are off")
for light in lightsJSON:
  if lightsJSON[light]['state']['on'] == False:
    print (light, '=', lightsJSON[light]['name']) 