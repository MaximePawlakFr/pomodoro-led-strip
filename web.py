from flask import Flask, render_template
from flask_socketio import SocketIO

import strip
import time
from threading import Thread

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
t = None

	
@app.route("/")
def index():
	socketio.emit('start_pomodoro', {'data': int(time.time())})
	return render_template("index.html", tomatoCount=strip.tomatoCount)

def checkThread():
	global t
	print 'start Strip'
	if t is not None and t.isAlive():
		print 't is not None'
		strip.stop = True
		t.join()
	elif t is None:
		print 't is None'	
		strip.init()

def clearStrip():
	global t
	checkThread()
	t = None
	return

def startStrip():
	global t
	checkThread()
	print 'strip ready'
	strip.stop = False
	t = Thread(target=strip.start)
	t.start()
	print 'strip started'

def pomodoroStarted(start_date):	
	print 'pomodoroStarted'
	socketio.emit('pomodoro_started', {'date': start_date})

def pomodoroPaused(start_date):	
	print 'pomodoroPaused'
	socketio.emit('pomodoro_paused', {'date': start_date})

@app.route("/start")
def hello():
	print 'hello'
#	start_date = int(time.time())
#	startStrip()
#	pomodoroStarted(start_date)
	return render_template("index.html", tomatoCount = strip.tomatoCount)

@app.route("/pause")
def pause():
	print 'pause'
	global t
	if t is not None and t.isAlive():
		print 'not none'
		strip.stop = True
		t.join()
	elif t is None:
		print 'else'	
		strip.init()
	print 'stopped'
	strip.stop = False
	t = Thread(target=strip.pause)
	t.start()
	return render_template("index.html")

def pauseStrip():
	print 'pause'
	global t
	checkThread()
	strip.stop = False
	t = Thread(target=strip.pause)
	t.start()

def demoStrip():
	print 'pause'
	global t
	checkThread()
	strip.stop = False
	t = Thread(target=strip.demo)
	t.start()

@app.route("/stop")
def stop():
	print 'stop'
	if t is not None:
		strip.stop = True
		t.join()
	print 'stopped'
	return render_template('index.html')

def stopStrip():
	if t is not None:
		strip.stop = True
		t.join()
	print 'stopped'
	return 0	

@app.route('/shutdown')
def shutdown():
	print 'shutdown'	
	socketio.stop()
	return "Shutdown !"

@socketio.on('message')
def handle_message(msg):
	print('received message: '+msg)

@socketio.on('my event')
def handle_message(msg):
	print('my event: ')

@socketio.on('connect')
def connect():
	print('Connected')
	
@socketio.on('start_pomodoro')
def handle_message():
	print('Start Pomodoro')
	start_date = int(time.time())
	print(start_date)
	startStrip()
	pomodoroStarted(start_date)
	
@socketio.on('pause_pomodoro')
def handle_message():
	print('Pause Pomodoro')
	start_date = int(time.time())
	print(start_date)
	pauseStrip()
	pomodoroPaused(start_date)
	
@socketio.on('stop_pomodoro')
def handle_message():
	print('Stop Pomodoro')
	stopStrip()
if __name__ == "__main__":
    # app.debug=True
    # app.run(host='0.0.0.0')
	socketio.run(app,host='0.0.0.0')
