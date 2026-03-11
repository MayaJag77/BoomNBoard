from django.db import models

class User(models.Model):
    userID = models.CharField(primary_key=True, max_length=128, unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return self.username

class Sounds(models.Model):
    soundID = models.CharField(primary_key=True, max_length=5, unique=True)
    saved_sounds = models.ManyToManyField(User, through='SavedSounds')
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    soundFile = models.URLField()
    name = models.CharField(max_length=40)
    category = models.CharField(default=0, max_length=15)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class SavedSounds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sound = models.ForeignKey(Sounds, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'sound')

    def __str__(self):
        return f"{self.user.username} saved {self.sound.name}"