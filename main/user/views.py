from django.shortcuts import render

def signin(request):
    context = {"name_page": "signin"}
    return render(request, "signin.html", context)

def signout(request):
    pass
    #context = {"name_page": "signout"}
    #return render(request, "profile.html", context)

def signup(request):
    context = {"name_page": "signup"}
    return render(request, "signup.html", context)