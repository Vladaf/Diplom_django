from django.urls import path
from user import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("signin/", views.signin, name="signin_page"),
    path("signout/", views.signout, name="signout_page"),
    path("signup/", views.Registration.as_view(), name="signup_page"),
    path("", lambda request: redirect(reverse("signin_page"))),
]