from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("catalog/", include("catalog.urls")),
    path("private/", include("private.urls")),
    path("", include("home.urls")),
]