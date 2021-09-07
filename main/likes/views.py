from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import View
from user.models import User
from private.models import Song
from likes.models import SongLikes

class AddLikeView(View):
    def post(self, request, *args, **kwargs):
        song_post_id = int(request.POST.get('song_post_id'))
        user_id = int(request.POST.get('user_id'))
        url_form = request.POST.get('url_form')

        user_inst = User.objects.get(id = user_id)
        song_post_inst = Song.objects.get(id = song_post_id)

        try:
            song_like_inst = SongLikes.objects.get(song_post = song_post_inst, liked_by = user_inst)
        except Exception as e:
            post_like = SongLikes(song_post = song_post_inst, liked_by = user_inst, like = True)
            post_like.save()

        return redirect(url_form)

class RemoveLikeView(View):
    def post(self, request, *args, **kwargs):
        song_likes_id = int(request.POST.get('song_likes_id'))
        url_form = request.POST.get('url_form')

        song_like = SongLikes.objects.get(id = song_likes_id)
        song_like.delete()

        return redirect(url_form)