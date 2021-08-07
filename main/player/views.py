from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from private.models import Song

def player(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj": page_obj}
    return render(request, "player.html", context)