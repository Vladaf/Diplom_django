# Generated by Django 3.2.3 on 2021-06-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=20, verbose_name='Band')),
                ('name', models.CharField(max_length=50, verbose_name='Song name')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('post_date', models.DateField(auto_now_add=True, verbose_name='Post date')),
                ('audio', models.FileField(upload_to='', verbose_name='Audio')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='private.album')),
                ('genre', models.ManyToManyField(related_name='genres', to='private.Genre')),
                ('likes', models.ManyToManyField(related_name='like', to='private.Likes')),
            ],
            options={
                'db_table': 'songs',
            },
        ),
    ]
