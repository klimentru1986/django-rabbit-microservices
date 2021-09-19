
from kafka.consumer.fetcher import ConsumerRecord


def consume_callback(msg: ConsumerRecord):
    print(msg.value)
