from rest_framework.generics import RetrieveAPIView

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Staff


class StaffRetrieveAPIView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


__all__ = ["StaffRetrieveAPIView"]
