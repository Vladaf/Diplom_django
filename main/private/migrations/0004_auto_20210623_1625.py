# Generated by Django 3.2.3 on 2021-06-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0003_alter_song_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
