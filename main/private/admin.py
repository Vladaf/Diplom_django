from django.contrib import admin
from private.models import *

class AdminSong(admin.ModelAdmin):
    list_display = ["band", "name"]

class AdminGenre(admin.ModelAdmin):
    list_display = ["name"]

class AdminPlaylist(admin.ModelAdmin):
    list_display = ["name", "playlist_author"]

class AdminSongPlaylist(admin.ModelAdmin):
    list_display = ["song", "playlist"]

admin.site.register(Song, AdminSong)
admin.site.register(Genre, AdminGenre)
admin.site.register(Playlist, AdminPlaylist)
admin.site.register(SongPlaylist, AdminSongPlaylist)