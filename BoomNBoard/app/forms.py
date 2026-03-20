from django import forms
from app.models import AppUser
from django.contrib.auth.models import User
from app.models import Sound

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class SoundUploadForm(forms.ModelForm):
    class Meta:
        model = Sound
        fields = ['name', 'soundFile', 'category', 'description']

