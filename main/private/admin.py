from django.contrib import admin
from private.models import Song, Album, Genre

class AdminSong(admin.ModelAdmin):
    list_display = ["band", "name"]

class AdminAlbum(admin.ModelAdmin):
    list_display = ["name"]

class AdminGenre(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Song, AdminSong)
admin.site.register(Album, AdminAlbum)
admin.site.register(Genre, AdminGenre)