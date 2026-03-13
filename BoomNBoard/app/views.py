from django.shortcuts import render
from django.http import HttpResponse
from app.models import Sound

def index(request):

    context_dict = {"aboutmessage": "Welcome to BoomNBoard the best place to play your favourite sounds!" ,
                    "aboutmessagecontinued" : "Click on a button to begin or login to an account to view your favourites!"
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