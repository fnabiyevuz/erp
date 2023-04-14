from rest_framework.generics import ListCreateAPIView

from apps.staff.api_endpoints.position.PositionListCreate.serializers import PositionSerializer
from apps.staff.models import Position


class PositionListCreateAPIView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


__all__ = ["PositionListCreateAPIView"]
