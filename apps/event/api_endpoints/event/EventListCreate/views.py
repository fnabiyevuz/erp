from rest_framework.generics import ListCreateAPIView

from apps.event.api_endpoints.event.EventListCreate.serializers import EventSerializer
from apps.event.models import Event


class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


__all__ = ["EventListCreateAPIView"]
