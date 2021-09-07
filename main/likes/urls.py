from django.urls import path, include
from django.urls.resolvers import URLPattern

from .views import AddLikeView, RemoveLikeView

app_name = "likes"

urlpatterns = [
    path("add/", AddLikeView.as_view(), name="add"),
    path("remove/", RemoveLikeView.as_view(), name="remove"),
]