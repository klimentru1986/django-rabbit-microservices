import pika

EXCHANGE_NAME='ping_exchange'
QUEUE_NAME='ping'

def create_channel(exchange):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='host.docker.internal',
            port=5672,
            credentials=pika.PlainCredentials('guest', 'guest')
        ))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    print("channel created", exchange)
    return channel


def send_message(channel, exchange, routing_key, body):
    channel.basic_publish(exchange=exchange,
                          routing_key=routing_key,
                          body=body)
    print(exchange, routing_key, body)


def consume_messages(channel, exchange, queue, callback):
    result = channel.queue_declare(queue, exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=queue_name)
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=callback)

    channel.start_consuming()


ping_channel = create_channel(EXCHANGE_NAME)
