from rest_framework.generics import RetrieveAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectSerializer
from apps.project.models import Project


class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectRetrieveAPIView"]
