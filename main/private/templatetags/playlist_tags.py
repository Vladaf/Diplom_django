from django import template
from private.forms import SongPlaylistForm

register = template.Library()

@register.simple_tag()
def form_tag():
    form = SongPlaylistForm()
    return form