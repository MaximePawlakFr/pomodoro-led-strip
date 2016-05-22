import pomodoro
import sys
try:

    pomodoro.setBrightness(10)
    pomodoro.start(numPixels=15, cycle_duration=5)
except:
    sys.exit(0)
