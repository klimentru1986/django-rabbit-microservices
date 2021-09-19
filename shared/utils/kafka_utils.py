from kafka import KafkaProducer, KafkaConsumer
import json
import time

kafka_config = {
    "bootstrap_servers": "kafka:9092",
    "sasl_plain_username": "user",
    "sasl_plain_password": "bitnami",
    "api_version": (0, 10, 0),
}


def send_message(topic: str, message: dict):
    producer = KafkaProducer(
        **kafka_config,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, message)


def get_messages(topic: str, callback):
    consumer = KafkaConsumer(topic, **kafka_config, group_id="pong", auto_offset_reset='earliest')
    for msg in consumer:
        callback(msg)
