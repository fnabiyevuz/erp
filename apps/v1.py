from django.urls import path, include

urlpatterns = [
    path("staff/", include("apps.staff.urls")),
    path("inventory/", include("apps.inventory.urls")),
    path("event/", include("apps.event.urls")),
    path("project/", include("apps.project.urls")),
]
