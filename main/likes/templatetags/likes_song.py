from django import template
from likes.models import SongLikes

register = template.Library()

@register.simple_tag(takes_context = True)
def is_liked(context, song_post_id):
    request = context['request']
    try:
        song_likes = SongLikes.objects.get(song_post__id = song_post_id, liked_by = request.user.id).like
    except Exception as e:
        song_likes = False
    return song_likes

@register.simple_tag()
def count_likes(song_post_id):
    return SongLikes.objects.filter(song_post__id = song_post_id, like = True).count()

@register.simple_tag(takes_context = True)
def song_likes_id(context, song_post_id):
    request = context['request']
    return SongLikes.objects.get(song_post__id = song_post_id, liked_by = request.user.id).id