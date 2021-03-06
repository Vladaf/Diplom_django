from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from private.forms import *
from private.models import *
from user.models import User
from likes.models import SongLikes

def profile(request):
    if request.user.is_authenticated:
        track_list = Song.objects.filter(post_author = request.user.username)
        playlist_list = Playlist.objects.filter(playlist_author = request.user.id)
        likes = SongLikes.objects.filter(liked_by = request.user.id)
        likes_list = []
        for like in likes:
            likes_list.append(like.song_post)
        context = {
            "track_list": track_list,
            "playlist_list": playlist_list,
            "likes_list": likes_list,
            }        
        return render(request, "profile.html", context)
    else:
        return redirect(reverse("signin_page"))

def upload(request):
    context = {"upload_form": UploadForm()}
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit = False)
            upload.post_author = request.user.username
            upload.save()
            return redirect(reverse("profile_page"))
        else:
            context["upload_form"] = upload_form
    return render(request, "upload.html", context)

def playlist(request):
    context = {"playlist_form": PlaylistForm()}
    if request.method == "POST":
        playlist_form = PlaylistForm(request.POST, request.FILES)
        if playlist_form.is_valid():
            playlist = playlist_form.save(commit = False)
            playlist.playlist_author = request.user
            playlist.save()
            return redirect(reverse("home_page"))
        else:
            context["playlist_form"] = playlist_form
    return render(request, "playlist.html", context)

class AddToPlaylistView(View):
    def post(self, request, *args, **kwargs):
        song_post_id = int(request.POST.get('song_post_id'))
        playlist_id = int(request.POST.get('playlist'))
        user_id = int(request.POST.get('user_id'))
        url_form = request.POST.get('url_form')

        user_inst = User.objects.get(id = user_id)
        song_post_inst = Song.objects.get(id = song_post_id)
        playlist_choice_inst = Playlist.objects.get(id = playlist_id)

        try:
            song_playlist_inst = SongPlaylist.objects.get(song = song_post_inst, playlist = playlist_choice_inst)
        except Exception as e:
            add_playlist = SongPlaylist(song = song_post_inst, playlist = playlist_choice_inst)
            add_playlist.save()

        return redirect(url_form)

class DeleteSongView(View):
    def post(self, request, *args, **kwargs):
        song_post_id = int(request.POST.get('song_post_id'))
        url_form = request.POST.get('url_form')

        song = Song.objects.get(id = song_post_id)
        song.delete()

        return redirect(url_form)

class DeletePlaylistView(View):
    def post(self, request, *args, **kwargs):
        playlist_id = int(request.POST.get('playlist_id'))
        url_form = request.POST.get('url_form')

        playlist = Playlist.objects.get(id = playlist_id)
        playlist.delete()

        return redirect(url_form)

def edit_song(request, song_id):
    song = Song.objects.get(id = song_id)
    context = {
        "song": song,
        "upload_form": UploadForm(instance = song)
        }
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES, instance = song)
        if upload_form.is_valid():
            upload = upload_form.save()
            return redirect(reverse("profile_page"))
        else:
            context["upload_form"] = upload_form
    return render(request, "edit_song.html", context)

def edit_playlist(request, playlist_id):
    playlist = Playlist.objects.get(id = playlist_id)
    context = {
        "playlist": playlist,
        "playlist_form": PlaylistForm(instance = playlist)
        }
    if request.method == "POST":
        playlist_form = PlaylistForm(request.POST, request.FILES, instance = playlist)
        if playlist_form.is_valid():
            upload = playlist_form.save()
            return redirect(reverse("profile_page"))
        else:
            context["upload_form"] = playlist_form
    return render(request, "edit_playlist.html", context)

