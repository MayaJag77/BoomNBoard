from django.shortcuts import render
from django.http import HttpResponse
from app.models import Sound, AppUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

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

@csrf_exempt  # For testing only — use CSRF token in production
def update_record(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            record_id = data.get("name")
            new_value = data.get("mp3")

            if not record_id or new_value is None:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            obj = Sound.objects.filter(id=SavedSound).first()
            if not obj:
                return JsonResponse({"error": "Record not found"}, status=404)

            obj.my_field = new_value
            obj.save()

            return JsonResponse({"success": True, "updated_value": obj.my_field})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

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
    return render(request, 'BoomNBoard/myaccount.html')

def categories(request): 
    return render(request, 'BoomNBoard/categories.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user:
            if user.is_active:
                login(request)
                return redirect(reverse('app:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'rango/login.html')

def checkUsername(request):
    username = request.GET.get("username")
    exists = User.objects.filter(username=username).exists()
    return HttpResponse({"exists": exists})
