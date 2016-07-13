import hue
import sys

light = hue.Light(sys.argv[1])
light.on()