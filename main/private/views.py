from django.shortcuts import render

def profile(request):
    context = {"name_page": "profile"}
    return render(request, "profile.html", context)