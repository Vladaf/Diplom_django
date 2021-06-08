from django.urls import path
from home import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("home/", views.home, name="home_page"),
    path("", lambda request:redirect (reverse("home_page"))),
]