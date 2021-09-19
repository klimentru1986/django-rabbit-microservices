# from ping_service.apps import PingServiceConfig
# from shared.utils.queue_utils import EXCHANGE_NAME, QUEUE_NAME, send_message
from django.urls.conf import path
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


from shared.utils.kafka_utils import send_message


class PingViewSet(GenericViewSet):

    @action(methods=['GET'], detail=False)
    def ping(self, request):
        send_message('ping', {"text": "hello"})
        return Response(status=status.HTTP_201_CREATED)


ping_urlpatterns = [
    path(r'ping', PingViewSet.as_view(
        {'get': 'ping'}), name='ping'),
]
