from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Sound, User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404
import os
from django.conf import settings

def index(request):

    context_dict = {"aboutmessage": "Welcome to BoomNBoard the best place to play your favourite sounds!" ,
                    "aboutmessagecontinued" : "Click on a button to begin or login to an account to view your favourites!",
                    "colourkey": [
                    {"colourkeycss": "meme",     "label": "Meme Sounds"},
                    {"colourkeycss": "ringtone", "label": "Ringtones"},
                    {"colourkeycss": "music",    "label": "Music"},
                    ],
                    }
    
    Trending_Sounds_List = Sound.objects.all()
    
    context_dict["TrendingSounds"] = Trending_Sounds_List

    return render(request, 'BoomNBoard/index.html', context=context_dict)

def login(request):
    return render(request, 'BoomNBoard/login.html')

def signup(request):
    return render(request, 'BoomNBoard/signup.html')

def help(request):
    return render(request, 'BoomNBoard/help.html')

def myaccount(request): 
    return render(request, 'BoomNBoard/myaccount.html')

def categories(request): 
    return render(request, 'BoomNBoard/categories.html')

@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "redirecting": "/"})
        else:
            return JsonResponse({"success": False, "error": "Invalid username or password"})

def check_username(request):
    username = request.GET.get("username")
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({"exists": exists})
