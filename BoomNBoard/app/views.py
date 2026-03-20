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
from app.forms import SoundUploadForm
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

@login_required
def myaccount(request):
    if not request.user.is_authenticated:
        return redirect('app:login')
    if request.method == 'POST':
        form = SoundUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sound = form.save(commit=False)
            sound.uploadedBy = request.user
            sound.save()
            messages.success(request, "Sound uploaded successfully!")
            return redirect('app:myaccount')
        else:
            messages.error(request, "Upload failed. Please check the form.")
    else:
        form = SoundUploadForm()

    uploaded_sounds = Sound.objects.filter(uploadedBy=request.user)
    saved = request.user.saved_sounds.all()


    context_dict = {
        'form': form,
        'UploadedSounds': uploaded_sounds,
        'FavouriteSounds': saved,
    }
    return render(request, 'BoomNBoard/myaccount.html', context=context_dict)

# @login_required
# def restricted(request):
#     return render(request, 'BoomNBoard/restricted.html')

@csrf_exempt
def save_fav(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            user_id = data.get("user_id")
            sound_id = data.get("sound_id")

            if not user_id or not sound_id:
                return JsonResponse({"error": "Missing user_id or sound_id"}, status=400)

            user = AppUser.objects.get(id=user_id)
            sound = Sound.objects.get(soundID=sound_id)

            SavedSound.objects.get_or_create(appuser=user, sound=sound)

            return JsonResponse({"message": "Sound saved"})
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


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