from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.list import ListView
from private.forms import UploadForm
from django.core.paginator import Paginator
from private.models import Song

def profile(request):
    context = {"name_page": "profile"}
    if request.user.is_authenticated:
        track_list = Song.objects.filter(post_author__exact = request.user.username)
        paginator= Paginator(track_list,1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"track_list": track_list, "page_obj": page_obj}
        return render(request, "profile.html", context)
    else:
        return redirect(reverse("signin_page"))

def upload(request):
    context = {"upload_form": UploadForm()}
    if request.method == "POST":
        upload_form = UploadForm(request.POST)
        if upload_form.is_valid():
            upload = upload_form.save(commit = False)
            upload.post_author = request.user.username
            upload.save()
            return redirect(reverse("home_page"))
        else:
            context["upload_form"] = upload_form
    return render(request, "upload.html", context)

def player(request):
    paginator= Paginator(Song.objects.filter(post_author__exact = request.user.username),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj": page_obj}
    return render(request, "player.html", context)