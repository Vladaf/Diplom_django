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
    counter = []
    for artist in artist_list:
        track_list = Song.objects.filter(band = artist)
        count = len(track_list)
        counter.append(count)
    artist_info = zip(artist_list, counter)
    context = {"artist_info": artist_info}
    return render(request, "artists.html", context)

def artists_detail(request, artist_name):
    #users_list = User.objects.filter(is_musician = True)
    artists_detail = User.objects.get(username = artist_name)
    if artists_detail:
        music_detail = Song.objects.filter(band = artist_name)
        context = {"artists_detail": artists_detail, "music_detail": music_detail}
        return render(request, "artists_detail.html", context)
    else:
        return redirect(reverse("home_page"))