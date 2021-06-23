from django.shortcuts import redirect, render
from django.urls.base import reverse
from private.forms import UploadForm

def profile(request):
    context = {"name_page": "profile"}
    if request.user.is_authenticated:
        return render(request, "profile.html", context)
    else:
        return redirect(reverse("signin_page"))

def upload(request):
    context = {"upload_form": UploadForm()}
    if request.method == "POST":
        upload_form = UploadForm(request.POST)
        if upload_form.is_valid():
            upload_form.save()
            return redirect(reverse("home_page"))
        else:
            context["upload_form"] = upload_form
    return render(request, "upload.html", context)