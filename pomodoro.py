# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from neopixel import *


# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Colors
blue = Color(0,0,255)
green = Color(255,0,0)
red = Color(0,255,0)
black = Color(0,0,0)

# Strip
s = None

tomatoCount = 0
stop = False

# Init the strip
def init():
	global s
	# Create NeoPixel object with appropriate configuration.
	s = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	s.begin()
	colorWipe(s, black)

def ready():
	global s
	colorWipe(s, green)


# Start the pomodoro for 25 minutes
# numPixels : how many
# cycle_duration : how long in seconds a led will blink
def start(strip, numPixels=25, start_color=green, done_color=red,  cycle_duration=60):
	# Wipe the strip with start color
	colorWipe(s, start_color)

	# Turn off additional leds
	colorRange(s, range(numPixels,LED_COUNT), black)

	start_date = int(time.time())

	pixel = numPixels - 1 # current pixel to blink

	while not stop and pixel >= 0:
		now = int(time.time())
		diff = (now - start_date)

		count = diff / cycle_duration
		if(count > 0):
			out = []
			for i in range(numPixels - count , numPixels):
				out.append(i)
			colorRange(s, out, done_color)

			# Update blinking pixel
			pixel = numPixels - 1 - count

		print 'time: ', now, start_date, diff, count
		if pixel < 0:
			print 'Done !'
			break

		else:
			blinkPixel(s, pixel)
	print 'Done.'

	# When done, blink all
	while not stop:
		blinkAll(s)
	return

# Pause pomodoro
def pause():
	global tomatoCount
	tomatoCount =  tomatoCount + 1
	start(numPixels=5, start_color=blue, done_color=red)

# Set strip brightness
def setBrightness(b):
	global s
	s.setBrightness(b)

# Increment brightness
def incBrightness(brightness):
	global s
	global LED_BRIGHTNESS
	b = LED_BRIGHTNESS
	b = b+brightness
	b = abs(b) if b < 255 else 255
	print b
	LED_BRIGHTNESS = b
	s.setBrightness(b)
