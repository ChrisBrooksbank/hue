import json
import requests

class Light():
	def __init__(self,lightname):
		self.lightname = lightname
		self.config = json.loads(open('config.json', 'r').read())
		self.bridgeaddress = self.config['hue']['bridgeaddress']
		self.bridgeusername = self.config['hue']['bridgeusername']
		self.lightnumber = 0
		url = 'http://' + self.config['hue']['bridgeaddress'] + '/api/' + self.config['hue']['bridgeusername'] + '/lights/'
		response = requests.get(url)
		lightsJSON = response.json()
		for lightindex in lightsJSON:
			if lightsJSON[lightindex]['name'] == lightname :
				self.lightnumber = lightindex
	
	def setstate(self,state):
		url = 'http://' + self.bridgeaddress + '/api/' + self.bridgeusername + '/lights/' + str(self.lightnumber) + '/state'
		response = requests.get(url)
		data = state
		response = requests.put(url, data=data)
			

	def on(self):
		self.setstate('{"on":true}')

	def off(self):
		self.setstate('{"on":false}')

	def dim(self):
		self.setstate('{"on":true,"bri":2}')

	def bright(self):
		self.setstate('{"on":true,"bri":254}')		

	def blink(self):
		self.setstate('{"alert":"select"}')

	def green(self):
		self.setstate('{"xy":[0.214,0.709]}')

	def red(self):
		self.setstate('{"xy":[0.6621,0.3023]}')

	def orange(Self):
		self.setstate('{"xy":[0.5614,0.4156]}')
