# hue.py

These python scripts allows you to control the (Phillips Hue) lights in your house.

## Configuration
Create a file called config.json to contain your Phillips Hue bridge address and username.
[Click here](http://www.developers.meethue.com/documentation/getting-started) to see how to find bridge address and create username on hue bridge

An example file is :
{
	"hue" : {
	"bridgeaddress" : "yourhuebridgeaddress",
	"bridgeusername" : "yourhuebridgeusername"
}
}

## Scripts
### hue.py 
This script is not designed to be called from the command line.
This contains the Light class which is the meat of this project.

Pass in the name of a light to its constructor e.g. light = hue.Light("landing")
You can then call methods such as on, off, dim, bright, blink, green, red, orange
## catlights.py
Can be called from command line.
Outputs a list of lights which are on and another list of lights which are off.
### off.py
Can be called from command line.
Pass in name of light to turn off.
### on.py
Can be called from command line.
Pass in name of light to turn on.
### dim.py
Can be called from command line.
Pass in name of light to dim.
### bright.py
Can be called from command line.
Pass in name of light to make brighter.
### green.py
Pass in name of light to make green.
### red.py
Pass in name of light to make red.
### orange.py
Pass in name of light to make orange.