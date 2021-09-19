from shared.utils.kafka_utils import get_messages
from pong_service.message_interceptor import consume_callback
from django.apps import AppConfig
from shared.utils.queue_utils import EXCHANGE_NAME, QUEUE_NAME, consume_messages


class PongServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pong_service'

    def __init__(self, *args, **kwargs):
        print('pong_service init')
        get_messages("ping", consume_callback)
        super().__init__(*args, **kwargs)
