from flask import Flask, render_template
from flask_socketio import SocketIO

import pomodoro
import time
from threading import Thread

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
t = None

def checkThread():
    global t
    print 'start Strip'
    if t is not None and t.isAlive():
		print 't is not None'
		pomodoro.STOP_FLAG = True
		t.join()
    elif t is None:
		print 't is None'	
    #strip.init()
    pomodoro.STOP_FLAG = False


def clearStrip():
	global t
	checkThread()
	t = None
	return

def startStrip(numPixels=-1):
    global t
    checkThread()
    print 'strip ready'
    # pomodoro.stop = False
    if numPixels>0:
        t = Thread(target=pomodoro.start, args=(numPixels,))
    else:
        t = Thread(target=pomodoro.start)
    t.start()
    print 'strip started'

def pauseStrip():
	print 'pause'
	global t
	checkThread()
	pomodoro.stop = False
	t = Thread(target=pomodoro.pause)
	t.start()

def stopStrip():
    print 'stop'
    checkThread()
    pomodoro.stop = False
    t = Thread(target=pomodoro.stop)
    t.start()
    
