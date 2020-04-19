import pika


# Make a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='postbox')

# Send a message to queue
channel.basic_publish(
    exchange='',                # Use default exchange, ignore it for now.
    routing_key='postbox',      # Specific queue name
    body='Hi there!',
)
print('Message was sent!')

# Flush network buffer to make sure message was sent to RabbitMQ
connection.close()
