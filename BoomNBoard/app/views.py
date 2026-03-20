from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from app.models import Sound, AppUser, SavedSound
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json

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
            return redirect('app:login')

        user = AppUser.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)

        return redirect('app:myaccount')
    return render(request, 'BoomNBoard/signup.html')

def help(request):
    return render(request, 'BoomNBoard/help.html')

def myaccount(request): 

    favouriteSoundsList = SavedSound.objects.all()

    context_dict = {}
    context_dict["FavouriteSounds"] = favouriteSoundsList

    return render(request, 'BoomNBoard/myaccount.html', context = context_dict)

# @login_required
# def restricted(request):
#     return render(request, 'BoomNBoard/restricted.html')

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

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return redirect('app:myaccount')

        messages.error(request, "Invalid username or password. Try again.")
        return redirect('app:login')

    return render(request, 'BoomNBoard/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('app:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val