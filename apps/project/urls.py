from django.urls import path
from .api_endpoints import service
from .api_endpoints import project_type
from .api_endpoints import project


urlpatterns = [
    path('service/', service.ServiceListAPIView.as_view(), name='service-list'),
    path('project-type/', project_type.ProjectTypeListAPIView.as_view(), name='project-type-list'),

    path('', project.ProjectCreateAPIView.as_view(), name='project-create'),
    path('list/', project.ProjectListAPIView.as_view(), name='project-list'),
    path('<int:pk>/detail/', project.ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('<int:pk>/update/', project.ProjectUpdateAPIView.as_view(), name='project-update'),
    path('<int:pk>/delete/', project.ProjectDestroyAPIView.as_view(), name='project-delete'),
]
