import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')

data = {
    'duration':20    
}
message = json.dumps(data)

channel.basic_publish(exchange='', routing_key='hello',body=message)

print '[x] sent'
connection.close()


