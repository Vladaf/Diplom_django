from django.contrib import admin
from likes.models import SongLikes

class AdminSongLikes(admin.ModelAdmin):
    list_display = ["song_post", "liked_by", "like", "created"]

admin.site.register(SongLikes, AdminSongLikes)