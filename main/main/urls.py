from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("catalog/", include("catalog.urls")),
    path("private/", include("private.urls")),
    path("", include("home.urls")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)