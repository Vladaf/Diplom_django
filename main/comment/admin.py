from django.contrib import admin
from comment.models import SongComments

class AdminSongComments(admin.ModelAdmin):
    list_display = ["song_post", "commented_by", "created"]

admin.site.register(SongComments, AdminSongComments)