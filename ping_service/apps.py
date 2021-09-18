from django.apps import AppConfig


class PingServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ping_service'

    def __init__(self, *args, **kwargs):
        print('ping_service init')
        super().__init__(*args, **kwargs)