from django.shortcuts import render

def discover(request):
    context = {"name_page": "discover"}
    return render(request, "discover.html", context)

def browse(request):
    context = {"name_page": "browse"}
    return render(request, "browse.html", context)

def charts(request):
    context = {"name_page": "charts"}
    return render(request, "charts.html", context)

def artists(request):
    context = {"name_page": "artists"}
    return render(request, "artists.html", context)