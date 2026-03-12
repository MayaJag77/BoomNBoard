from django.contrib import admin
from app.models import Sound, User, SavedSound

# Register your models here.
admin.site.register(Sound)
admin.site.register(User)
admin.site.register(SavedSound)
