from django.urls import path
from .api_endpoints import staff
from .api_endpoints import position
from .api_endpoints import attendance


urlpatterns = [
    path('create/', staff.StaffCreateAPIView.as_view(), name='staff-create'),
    path('list/', staff.StaffListAPIView.as_view(), name='staff-list'),
    path('delete/<int:pk>/', staff.StaffDestroyAPIView.as_view(), name='staff-delete'),
    path('detail/<int:pk>/', staff.StaffRetrieveAPIView.as_view(), name='staff-detail'),
    path('update/<int:pk>/', staff.StaffUpdateAPIView.as_view(), name='staff-update'),
    path('position/', position.PositionListCreateAPIView.as_view(), name='position'),
    path('position/<int:pk>/', position.PositionRetrieveUpdateDestroyAPIView.as_view(),
         name='position-retrieve-update-destroy'),
    path('attendance/', attendance.AttendanceListAPIView.as_view(), name='attendance-list'),
]
