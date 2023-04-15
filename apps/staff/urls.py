from django.urls import path
from .api_endpoints import staff
from .api_endpoints import position
from .api_endpoints import attendance

urlpatterns = [
    path('create/', staff.StaffCreateAPIView.as_view(), name='staff-create'),
    path('list/', staff.StaffListAPIView.as_view(), name='staff-list'),
    path('<int:pk>/delete/', staff.StaffDestroyAPIView.as_view(), name='staff-delete'),
    path('<int:pk>/detail/', staff.StaffRetrieveAPIView.as_view(), name='staff-detail'),
    path('<int:pk>/update/', staff.StaffUpdateAPIView.as_view(), name='staff-update'),
    path('<int:pk>/attendance/', staff.StaffAttendanceListAPIView.as_view(), name='staff-attendance'),

    path('position/', position.PositionListCreateAPIView.as_view(), name='position'),
    path('<int:pk>/position/', position.PositionRetrieveUpdateDestroyAPIView.as_view(),
         name='position-retrieve-update-destroy'),

    path('attendance/', attendance.AttendanceCreateAPIView.as_view(), name='attendance-create'),
    path('attendance/list/', attendance.AttendanceListAPIView.as_view(), name='attendance-list'),
]
