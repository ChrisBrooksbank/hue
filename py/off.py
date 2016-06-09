import json
import requests
import sys

config = json.loads(open('config.json', 'r').read())

lightname = sys.argv[1]

url = 'http://' + config['hue']['bridgeaddress'] + '/api/' + config['hue']['bridgeusername'] + '/lights/'
response = requests.get(url)

lightsJSON = response.json()

for lightnumber in lightsJSON:
  if lightsJSON[lightnumber]['name'] == lightname :
    url = 'http://' + config['hue']['bridgeaddress'] + '/api/' + config['hue']['bridgeusername'] + '/lights/' + str(lightnumber) + '/state'
    data = '{"on":false}'
    response = requests.put(url, data=data)