from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from app.models import Sound, AppUser, SavedSound
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404
import os, json
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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('app:signup')

        if AppUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('app:signup')

        if AppUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('app:signup')

        user = AppUser.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('app:myaccount')
    return render(request, 'BoomNBoard/signup.html')

def help(request):
    return render(request, 'BoomNBoard/help.html')

def myaccount(request): 

    favouriteSoundsList = SavedSound.objects.all()

    context_dict = {}
    context_dict["FavouriteSounds"] = favouriteSoundsList

    return render(request, 'BoomNBoard/myaccount.html', context = context_dict)

@csrf_exempt
def save_fav(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            appuser = data.get("appuser")
            sound = data.get("sound")

            if not(appuser and sound):
                return JsonResponse({"error": "Song name and mp3 are required"}, status=400)
            
            song = SavedSound.objects.create(appuser=appuser, sound=sound)
            return JsonResponse({"message": "Song saved"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"Error": "Invalid request method"}, status=405)

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
    exists = AppUser.objects.filter(username=username).exists()
    return JsonResponse({"exists": exists})