import sys

import pika


# Make a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='postbox', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World..."

# Send a message to queue
channel.basic_publish(
    exchange='',                # Use default exchange, ignore it for now.
    routing_key='postbox',      # Specific queue name
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,      # Make message persistent
    )
)
print('Message was sent!')

# Flush network buffer to make sure message was sent to RabbitMQ
connection.close()
