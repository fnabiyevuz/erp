from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.inventory.api_endpoints.inventory.InventoryListCreate.serializers import InventorySerializer
from apps.inventory.models import Inventory


class InventoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


__all__ = ["InventoryRetrieveUpdateDestroyAPIView"]
