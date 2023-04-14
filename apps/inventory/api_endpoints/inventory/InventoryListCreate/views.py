from rest_framework.generics import ListCreateAPIView

from apps.inventory.api_endpoints.inventory.InventoryListCreate.serializers import InventorySerializer
from apps.inventory.models import Inventory


class InventoryListCreateAPIView(ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


__all__ = ["InventoryListCreateAPIView"]
