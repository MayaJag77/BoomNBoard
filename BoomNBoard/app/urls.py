from django.urls import path
from app import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('help/', views.help, name = 'help'),
    path('myaccount/', views.myaccount, name = 'myaccount'),
    path('categories/', views.categories, name='categories'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('checkUsername/', views.check_username),
    path('login/', views.loginUser, name='login'),
    path("save-fav/", views.save_fav, name='save_fav'),
    # path("update/", views.update_record, name="update_record"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
