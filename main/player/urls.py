from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from player import views

urlpatterns = [
    path("", views.player, name="player"),
]