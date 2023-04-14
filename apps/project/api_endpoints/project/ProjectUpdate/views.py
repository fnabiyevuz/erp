from rest_framework.generics import UpdateAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectSerializer
from apps.project.models import Project


class ProjectUpdateAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectUpdateAPIView"]
