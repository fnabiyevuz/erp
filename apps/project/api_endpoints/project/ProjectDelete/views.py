from rest_framework.generics import DestroyAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectSerializer
from apps.project.models import Project


class ProjectDestroyAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectDestroyAPIView"]
