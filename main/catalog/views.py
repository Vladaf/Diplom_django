from django.shortcuts import redirect, render
from django.urls.base import reverse
from datetime import datetime, date, time, timedelta
from django.views.generic.list import ListView
from private.forms import UploadForm
from private.models import Song, Genre
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


def browse(request, genre_name):
    genres_list = Genre.objects.all()
    if genre_name == 'all':
        genre_now = 'All'
        music_list = Song.objects.all()    
    else:
        genre_now = Genre.objects.get(name = genre_name)
        music_list = Song.objects.filter(genre = genre_now.id)
    context = {
            "genres_list": genres_list,
            "genre_now": genre_now,
            "music_list": music_list,
            }
    return render(request, "browse.html", context)


def charts(request, chart_name):
    date_live = date.today()
    if chart_name == 'all_the_time':
        chart_now = 'All the time'
        charts_list = Song.objects.all()
    elif chart_name == 'last_week':
        past_date = date_live - timedelta(days=7)
        chart_now = 'Last week'
        charts_list = Song.objects.filter(post_date__range=[past_date, date_live])
    elif chart_name == 'last_month':
        past_date = date_live - timedelta(days=30)
        chart_now = 'Last month'
        charts_list = Song.objects.filter(post_date__range=[past_date, date_live])
    else:
        past_date = date_live - timedelta(days=365)
        chart_now = 'Last year'
        charts_list = Song.objects.filter(post_date__range=[past_date, date_live])
        
    context = {
        "chart_now": chart_now,
        "charts_list": charts_list,
        }
    return render(request, "charts.html", context)


def artists(request):
    artist_list = User.objects.filter(is_musician = True)
    counter = []
    for artist in artist_list:
        count = Song.objects.filter(band = artist).count()
        counter.append(count)
    artist_info = zip(artist_list, counter)
    context = {"artist_info": artist_info}
    return render(request, "artists.html", context)


def artists_detail(request, artist_name):
    artist_detail = User.objects.get(username = artist_name)
    if artist_detail:
        music_detail = Song.objects.filter(band = artist_name)

        songs_count = music_detail.count()

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