from django.urls import path
from app import views
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('help/', views.help, name = 'help'),
    path('myaccount/', views.myaccount, name = 'myaccount'),
    path('categories/', views.categories, name='categories'),
    path('login/', views.loginUser, name='login'),
]
