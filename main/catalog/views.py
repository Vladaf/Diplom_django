from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.list import ListView
from private.forms import UploadForm
from private.models import Song
from user.models import User

def profile(request):
    context = {"name_page": "profile"}
    if request.user.is_authenticated:
        track_list = Song.objects.filter(post_author = request.user.username)
        context = {"track_list": track_list}
        return render(request, "profile.html", context)
    else:
        return redirect(reverse("signin_page"))

def discover(request):
    context = {"name_page": "discover"}
    return render(request, "discover.html", context)

def browse(request):
    context = {"name_page": "browse"}
    return render(request, "browse.html", context)

def charts(request):
    context = {"name_page": "charts"}
    return render(request, "charts.html", context)

def artists(request):
    artist_list = User.objects.filter(is_musician = True)
    track_list = Song.objects.filter(band = artist_list)
    context = {"artist_list": artist_list}
    return render(request, "artists.html", context)