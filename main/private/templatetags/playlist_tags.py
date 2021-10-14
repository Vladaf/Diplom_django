from django import template
from private.forms import SongPlaylistForm
from private.models import Playlist

register = template.Library()

@register.simple_tag(takes_context = True)
def form_tag(context):
    request = context['request']
    form = SongPlaylistForm()
    #form.fields['playlist'] = Playlist.objects.filter(playlist_author = request.user.id)
    return form