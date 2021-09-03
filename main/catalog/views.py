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
    artist_detail = User.objects.get(username = artist_name)
    if artist_detail:
        music_detail = Song.objects.filter(band = artist_name)

        songs_count = len(music_detail)

        albums_set = set()
        for song in music_detail:
            albums_set.add(song.album)
        albums_count = len(albums_set)
        albums_ = []
        for album_ in albums_set:
            albums_.append(Song.objects.filter(album = album_).first())
        albums_picture = []
        for album in albums_:
            albums_picture.append(album.picture.url)
        albums_detail = zip(albums_set, albums_picture)

        genres_set = set()
        for song in music_detail:
            genres_set.add(song.genre)

        context = {
            "artist_detail": artist_detail,
            "music_detail": music_detail,
            "songs_count": songs_count,
            "albums_detail": albums_detail,
            "albums_count": albums_count,
            "genres_set": genres_set,
            }
        return render(request, "artists_detail.html", context)
    else:
        return redirect(reverse("home_page"))

def albums_detail(request, artist_name, album_name):
    artist_detail = User.objects.get(username = artist_name)
    album_detail = Song.objects.filter(album = album_name)

    songs_count = len(album_detail)

    genres_set = set()
    for song in album_detail:
        genres_set.add(song.genre)


    context = {
        "artist_detail": artist_detail,
        "album_detail": album_detail,
        "album_name": album_name,
        "songs_count": songs_count,
        "genres_set": genres_set,
        }
    return render(request, "albums_detail.html", context)