from rest_framework.generics import ListAPIView

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Staff
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StaffListAPIView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['position']
    search_fields = ['full_name']


__all__ = ["StaffListAPIView"]
