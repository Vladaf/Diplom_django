from django.contrib import admin
from private.models import Song, Genre

class AdminSong(admin.ModelAdmin):
    list_display = ["band", "name"]

class AdminGenre(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Song, AdminSong)
admin.site.register(Genre, AdminGenre)