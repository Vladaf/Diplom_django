from django.urls import path
from private import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("", views.profile, name="profile_page"),
]