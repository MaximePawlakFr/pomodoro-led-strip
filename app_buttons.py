import sys
import RPi.GPIO as GPIO
import time
import app 
import gaugette.rotary_encoder
import strip
import subprocess
import strip

A_PIN = 7
B_PIN = 9
halt_gpio = 2
# encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)

led_gpio = 23

GPIO.setmode(GPIO.BCM)
start_gpio = 17
pause_gpio = 27
stop_gpio = 22

GPIO.setup(start_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pause_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stop_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(halt_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('Started...')
GPIO.setup(led_gpio, GPIO.OUT)
GPIO.output(led_gpio, 1)
strip.Strip().strip.setBrightness(10)
try:
	while True:
#		delta = encoder.get_delta()
#		if delta!=0:
#			print "rotate %d" % delta
#			strip.setBrightness(delta)

		start = GPIO.input(start_gpio)

		pause = GPIO.input(pause_gpio)
		stop = GPIO.input(stop_gpio)
		if start == False:
			print('button pressed')
			app.startStrip()
			time.sleep(0.2)	
		if pause == False:
			print('button pressed')
			app.pauseStrip()
			time.sleep(0.2)
		if stop == False:
			print('button pressed')
			app.demoStrip()
			time.sleep(0.2)
#		halt = GPIO.input(halt_gpio)
		halt = True
		if halt == False:
			print('halt button pressed')
			# web.demoStrip()
			subprocess.call(["shutdown", "-h", "now"])
			time.sleep(0.2)

except KeyboardInterrupt:
	print "Keyboard interrupt"
	raise	
finally :
    print "stopping..."
    GPIO.output(led_gpio, 0)
    app.stopStrip()
    time.sleep(5)
    GPIO.cleanup()
    sys.exit(0)
