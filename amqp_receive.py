import pika
import app
import strip
import simplejson

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('[x] received %r' %body)
    strip.Strip().strip.setBrightness(10)
    try:
        data = simplejson.loads(body)
        duration = data['duration']
        print duration
        app.startStrip(numPixels=duration)    
    except KeyboardInterrupt:
        print 'Error'

channel.basic_consume(callback, queue='hello', no_ack=True)
print '[*] waiting ...'

channel.start_consuming()
