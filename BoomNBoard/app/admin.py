from django.contrib import admin
from app.models import Sound, AppUser, SavedSound

# Register your models here.
admin.site.register(Sound)
admin.site.register(AppUser)
admin.site.register(SavedSound)
