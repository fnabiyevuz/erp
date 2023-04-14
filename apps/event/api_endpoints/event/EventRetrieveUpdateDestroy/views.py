from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.event.api_endpoints.event.EventListCreate.serializers import EventSerializer
from apps.event.models import Event


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


__all__ = ["EventRetrieveUpdateDestroyAPIView"]
