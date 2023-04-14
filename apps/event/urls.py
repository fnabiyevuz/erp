from django.urls import path
from .api_endpoints import event


urlpatterns = [
    path('', event.EventListCreateAPIView.as_view(), name='event'),
    path('<int:pk>/', event.EventRetrieveUpdateDestroyAPIView.as_view(),
         name='event-retrieve-update-destroy'),
]
