from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.list import ListView
from private.forms import *
from private.models import *
from likes.models import SongLikes

def profile(request):
    if request.user.is_authenticated:
        track_list = Song.objects.filter(post_author = request.user.username)
        playlist_list = Playlist.objects.filter(playlist_author = request.user.id)
        likes = SongLikes.objects.filter(liked_by = request.user.id)
        likes_list = []
        for like in likes:
            likes_list.append(like.song_post)
        if request.method == "POST":
            songplaylist_form = SongPlaylistForm(request.POST)
            if songplaylist_form.is_valid():
                #playlist = songplaylist_form.save(commit = False)
                #playlist.song = Song.objects.get()
                songplaylist_form.save()
        context = {
            "track_list": track_list,
            "playlist_list": playlist_list,
            "likes_list": likes_list,
            "songplaylist_form": SongPlaylistForm()
            }        
        return render(request, "profile.html", context)
    else:
        return redirect(reverse("signin_page"))

def upload(request):
    context = {"upload_form": UploadForm()}
    if request.method == "POST":
        upload_form = UploadForm(request.POST)
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
        playlist_form = PlaylistForm(request.POST)
        if playlist_form.is_valid():
            playlist = playlist_form.save(commit = False)
            playlist.playlist_author = request.user.id
            playlist.save()
            return redirect(reverse("home_page"))
        else:
            context["playlist_form"] = playlist_form
    return render(request, "playlist.html", context)