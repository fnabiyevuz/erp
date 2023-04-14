from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.staff.api_endpoints.position.PositionListCreate.serializers import PositionSerializer
from apps.staff.models import Position


class PositionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


__all__ = ["PositionRetrieveUpdateDestroyAPIView"]
