from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {"aboutmessage": "Welcome to BoomNBoard the best place to play your favourite sounds!" ,
                    "aboutmessagecontinued" : "Click on a button to begin or login to an account to view your favourites!",
                    "colourkeymessage" : "Red - Meme sounds    Blue - Ringtones    Green - Music"
                    }

    return render(request, 'BoomNBoard/index.html', context=context_dict)

def login(request):
    return render(request, 'BoomNBoard/login.html')

def signup(request):
    return render(request, 'BoomNBoard/signup.html')

def help(request):
    return render(request, 'BoomNBoard/help.html')

def myaccount(request): 
    return render(request, 'BoomNBoard/myaccount.html')