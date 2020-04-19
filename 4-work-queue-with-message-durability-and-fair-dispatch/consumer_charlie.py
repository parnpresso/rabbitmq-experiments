import time

import pika


# Make a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='postbox', durable=True)

# Consume data from queue
def callback(ch, method, properties, body):
    print(f'Received: {body}')
    time.sleep(body.count(b'.'))
    print('Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Before consume, allow only 1 task at a time (Fair dispatch)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='postbox',
    on_message_callback=callback,
)

channel.start_consuming()
