from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey


class Song(models.Model):
    post_author = models.CharField(
        max_length = 100,
        verbose_name = "Author of the post",
    )
    band = models.CharField(
        max_length = 100,
        verbose_name = "Band",
    )
    name = models.CharField(
        max_length = 50,
        verbose_name = "Song",
    )
    album = models.CharField(
        max_length = 50,
        verbose_name = "Album",
    )
    post_date = models.DateField(
        auto_now_add = True,
        verbose_name = "Post date",
    )
    genre = models.ForeignKey(
        "Genre",
        on_delete=models.CASCADE
    )
    audio = models.FileField(
        blank=True,
        null=True,
        verbose_name = "Audio",
    )
    picture = models.ImageField(
        verbose_name = "Picture",
    )
    counter = models.IntegerField(
        default = 0,
        verbose_name = "Listening counter",
    )
    
    class Meta:
        db_table = "songs"

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(
        max_length = 30,
    )
    class Meta:
        db_table = "genres"
    def __str__(self):
        return self.name