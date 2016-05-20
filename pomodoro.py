# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from strip import *

tomatoCount = 0
stop = False

# Init the strip
def init():
    s = Strip()
    colorWipe(s.strip, black)

# Start the pomodoro for 25 minutes
# numPixels : how many
# cycle_duration : how long in seconds a led will blink
def start(numPixels=25, start_color=green, done_color=red,  cycle_duration=60):
    s = Strip().strip

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
