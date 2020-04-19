import pika


# Make a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='postbox')

# Consume data from queue
def callback(ch, method, properties, body):
    print(f'Received: {body}')

channel.basic_consume(
    queue='postbox',
    auto_ack=True,
    on_message_callback=callback,
)

channel.start_consuming()
