from django.db import models
from django.db.models.fields.related import ForeignKey


class Song(models.Model):
    band = models.CharField(
        max_length = 50,
        verbose_name = "Band",
    )
    name = models.CharField(
        max_length = 50,
        verbose_name = "Song name",
    )
    album = models.ForeignKey(
        "Album",
        null = True,
        on_delete = models.CASCADE,
        related_name="album",
    )
    post_date = models.DateField(
        auto_now_add = True,
        verbose_name = "Post date",
    )
    genre = models.ManyToManyField(
        "Genre",
        related_name="genres",
    )
    audio = models.FileField(
        verbose_name = "Audio",
    )
    picture = models.ImageField(
        verbose_name = "Picture",
    )
    class Meta:
        db_table = "songs"

    def str(self):
        return self.name


class Album(models.Model):
    name = models.CharField(
        max_length = 30,
    )
    class Meta:
        db_table = "albums"
    def str(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length = 30,
    )
    class Meta:
        db_table = "genres"
    def str(self):
        return self.name