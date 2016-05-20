# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from neopixel import *


# LED strip configuration:
LED_COUNT      = 160      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

blue = Color(0,0,255)
green = Color(255,0,0)
red = Color(0,255,0)
black = Color(0,0,0)






def blinkPixel(strip, pixel, speed=1000):
	blinkPixels(strip, [pixel])

# Blink the pixels at the speed param
def blinkPixels(strip, pixels, speed=1000):
	colors = []
	for pixel in pixels:
		colors.append(strip.getPixelColor(pixel))
#	print 'Color: ',curr_color, black
		strip.setPixelColor(pixel, black)
	strip.show()
	time.sleep(speed/1000.0)

	for i,pixel in enumerate(pixels):
		strip.setPixelColor(pixel, colors[i])

	strip.show()
	time.sleep(speed/1000.0)

# Blink all the strip
def blinkAll(strip, speed=1000):
	pixels = range(strip.numPixels())
	blinkPixels(strip, pixels, speed)

# Color a set of pixels
def colorRange(strip, pixels, color):
	for p in pixels:
		strip.setPixelColor(p, color)
	strip.show()


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
def multipleLines(strip, ledPerLines=20):
	print 'multipleLines'
	# Create NeoPixel object with appropriate configuration.
	#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	#strip.begin()
	numLines = strip.numPixels()/ledPerLines
	print str(numLines) + ' lines'
	print str(strip.numPixels()) + 'pixels'
	color = Color(255,0,0)
	wait_ms = 50
	"""Wipe color across display a pixel at a time."""
	for i in range(ledPerLines):
		for l in range(numLines):
			if l%2 == 0:
				pixel = i+l*ledPerLines
			else:
				pixel = (l+1)*ledPerLines - i -1
#			print pixel
			strip.setPixelColor(pixel, color)
		print 'Show'
		strip.show()
		time.sleep(wait_ms/1000.0)
		print 'Slept'
	print 'done'

def getPixelPosition(horizontalPosition, lineNumber, ledPerLines):
	i = horizontalPosition
	l = lineNumber
	if lineNumber%2 == 0:
		pixel = i+l*ledPerLines
	else:
		pixel = (l+1)*ledPerLines - i -1
	return pixel

def setColumnColor(strip, column, ledPerLines, color):
	print ledPerLines
	numLines = strip.numPixels()/ledPerLines
	i = column
	for l in range(numLines):
		if l%2 == 0:
			pixel = i+l*ledPerLines
		else:
			pixel = (l+1)*ledPerLines - i-1
#			print pixel
		strip.setPixelColor(pixel, color)
	strip.show()

def drawFigure(strip, fig, ledPerLines, offset=0, lineOffset=0):
	zero = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
	one = [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
	two = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
	three = [[1,1,1],[0,0,1],[0,1,1],[0,0,1],[1,1,1]]
	four = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
	five = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
	six = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
	seven = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
	eight = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
	nine = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]

	figures = [zero, one, two, three, four, five, six, seven, eight, nine]
	figure = figures[fig]

	for i in range(5):
		print 'line '+str(i)
		line = figure[i]
		for j in range(3):

			pixel = getPixelPosition(j+offset, i+lineOffset, ledPerLines)
			p = line[j]
			print str(p)+' -> '+ str(pixel)
			if p == 1:
				color = Color(0,255,0)
			else:
				color = Color(0,0,0)
			strip.setPixelColor(pixel, color)
	strip.show()

def column():
	global s
	init()
	ledPerLines = 20

	multipleLines(s)

	# column = 5
	#setColumnColor(s, column, ledPerLines, Color(0,0,255))
	print 'Draw figures'
	now = time.time()
	m, s = divmod(now, 60)
	h, m = divmod(m, 60)
	print '%d:%02d:%02d' % (h, m,s)

	drawFigure(s, 1, ledPerLines,0, 1)
	drawFigure(s, 9, ledPerLines, 4, 1)
	drawFigure(s, 1, ledPerLines, 8, 1)
	for i in range(10):

		drawFigure(s, i, ledPerLines, 12, 1)
		time.sleep(1)
	drawFigure(s, 2, ledPerLines, 8, 1)
	time.sleep(2)
	drawFigure(s, 3, ledPerLines, 12, 1)
	time.sleep(2)
	drawFigure(s, 4, ledPerLines, 16, 1)
	time.sleep(2)
	drawFigure(s, 5, ledPerLines,0,1 )
	time.sleep(2)
	drawFigure(s, 6, ledPerLines, 4, 1)
	time.sleep(2)
	drawFigure(s, 7, ledPerLines, 8, 1)
	time.sleep(2)
	drawFigure(s, 8, ledPerLines, 12, 1)
	time.sleep(2)
	drawFigure(s, 9, ledPerLines, 16, 1)
	time.sleep(2)
	drawFigure(s, 3, ledPerLines, 0, 1)

def clear():
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()
	exit()

def demo():
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while not stop:
		# Color wipe animations.
		colorWipe(strip, Color(255, 0, 0))  # Red wipe
		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
		colorWipe(strip, Color(0, 0, 255))  # Green wipe
		if stop:
			return
		# Theater chase animations.
		theaterChase(strip, Color(127, 127, 127))  # White theater chase
		if stop:
			return
		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		if stop:
			return
		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		if stop:
			return
		# Rainbow animations.
		rainbow(strip)
		if stop:
			return
		rainbowCycle(strip)
		if stop:
			return
		theaterChaseRainbow(strip)

if __name__ == '__main__':
	demo()
