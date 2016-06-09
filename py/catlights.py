import sys
import requests

huebridgeaddress = "192.168.1.103"
hueusername = "hS582W-AhSdUEE7Tfjll2xslcgFOTOEglDTOZTpA"

url = 'http://' + huebridgeaddress + '/api/' + hueusername + '/lights/'
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