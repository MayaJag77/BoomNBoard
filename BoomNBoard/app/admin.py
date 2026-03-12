from django.contrib import admin
from app.models import Sounds, User, SavedSounds

# Register your models here.
admin.site.register(Sounds)
admin.site.register(User)
admin.site.register(SavedSounds)
