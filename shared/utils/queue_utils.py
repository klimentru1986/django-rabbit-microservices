import pika
from datetime import datetime

EXCHANGE_NAME = 'ping_exchange'
QUEUE_NAME = 'ping'


def create_channel(exchange):
    print('connect start', datetime.now())
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='host.docker.internal',
            port=5672,
            credentials=pika.PlainCredentials('guest', 'guest')
        ))
    channel = connection.channel()
    print("channel created", exchange, datetime.now())
    return channel


def send_message(exchange, routing_key, body):
    channel = create_channel(exchange)

    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=body)
    print(exchange, routing_key, body)
    channel.close()


def consume_messages(exchange, queue, callback):
    channel = create_channel(exchange)

    channel.basic_consume(queue=queue,
                          auto_ack=True,
                          on_message_callback=callback)

    channel.start_consuming()
    channel.close()
