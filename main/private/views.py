from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic.list import ListView
from private.forms import UploadForm
from private.models import Song

def profile(request):
    context = {"name_page": "profile"}
    if request.user.is_authenticated:
        track_list = Song.objects.filter(post_author__exact = request.user.username)
        context = {"track_list": track_list}
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
