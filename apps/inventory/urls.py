from django.urls import path
from .api_endpoints import inventory


urlpatterns = [
    path('', inventory.InventoryListCreateAPIView.as_view(), name='inventory'),
    path('<int:pk>/', inventory.InventoryRetrieveUpdateDestroyAPIView.as_view(),
         name='inventory-retrieve-update-destroy'),
]
