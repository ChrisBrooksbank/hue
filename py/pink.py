import json
import requests

config = json.loads(open('config.json', 'r').read())

url = 'http://' + config['hue']['bridgeaddress'] + '/api/' + config['hue']['bridgeusername']  + '/lights/'
response = requests.get(url)

lightsJSON = response.json()

for lightnumber in lightsJSON:
  url = 'http://' + config['hue']['bridgeaddress'] + '/api/' + config['hue']['bridgeusername']  + '/lights/' + str(lightnumber) + '/state'
  data = '{"xy":[0.5454,0.2359]}'
  response = requests.put(url, data=data)