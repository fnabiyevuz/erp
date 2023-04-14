from rest_framework.generics import UpdateAPIView

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Staff


class StaffUpdateAPIView(UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


__all__ = ["StaffUpdateAPIView"]
