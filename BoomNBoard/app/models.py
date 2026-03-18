from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    def __str__(self):
        return self.username

class Sound(models.Model):
    savedSound = models.ManyToManyField(AppUser,through='SavedSound', related_name="saved_sounds")
    uploadedBy = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="uploaded_sounds")
    soundID = models.CharField(primary_key=True, max_length=5, unique=True)
    soundFile = models.URLField()
    name = models.CharField(max_length=40)
    category = models.CharField(default=0, max_length=15)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class SavedSound(models.Model):
    appuser = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('appuser', 'sound')

    def __str__(self):
        return f"{self.appuser.username} saved {self.sound.name}"