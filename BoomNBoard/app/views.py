from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {"aboutmessage": "Welcome to BoomNBoard the best place to play your favourite sounds!"}

    return render(request, 'BoomNBoard/index.html', context=context_dict)

def login(request):
    return render(request, 'BoomNBoard/login.html')

def signup(request):
    return render(request, 'BoomNBoard/signup.html')

def help(request):
    return render(request, 'BoomNBoard/help.html')