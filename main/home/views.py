from django.shortcuts import render

def home(request):
    context = {"name_page": "home"}
    return render(request, "home.html", context)