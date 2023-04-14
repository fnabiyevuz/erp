from rest_framework.generics import ListAPIView

from apps.project.api_endpoints.service.ServiceList.serializers import ServiceSerializer
from apps.project.models import Service


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


__all__ = ["ServiceListAPIView"]
