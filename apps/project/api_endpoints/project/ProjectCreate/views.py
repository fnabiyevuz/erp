from rest_framework.generics import CreateAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectSerializer
from apps.project.models import Project


class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectCreateAPIView"]
