import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BoomNBoard.settings')

import django
django.setup()
from django.contrib.auth.models import User
from app.models import User, Sound, SavedSound

def populate():
    User.objects.all().delete()

    user1 = User.objects.create(
        userID = "00001",
        username="karateDog7",
        email="alexKarateLover@test.com",
        password="testPassword"
    )

    user2 = User.objects.create(
        userID = "00002",
        username="noobmaster69",
        email="NoobTester@test.com",
        password="testPassword"
    )

    user3 = User.objects.create(
        userID = "00003",
        username="pterodactyl4",
        email="iLovePterodactyl@test.com",
        password="password12345"
    )

    sound1 = Sound.objects.create(
        soundID="00001",
        soundFile="BoomNBoard\static\audio\drums.mp3",
        name="Drum",
        category="Music",
        description="Loud Drums",
        uploadedBy=user1
    )

    sound2 = Sound.objects.create(
        soundID="00002",
        soundFile="BoomNBoard\static\audio\cat.mp3",
        name="Meow",
        category="Memes",
        description="This is a cat meowing.",
        uploadedBy=user2
    )

    sound3 = Sound.objects.create(
        soundID="00003",
        soundFile="BoomNBoard\static\audio\chatting.mp3",
        name="Yapping",
        category="Memes",
        description="This is someone saying something.",
        uploadedBy=user2
    )

    sound4 = Sound.objects.create(
        soundID="00004",
        soundFile="BoomNBoard\static\audio\roar.mp3",
        name="Dinosaur Roar",
        category="Memes",
        description="Roar",
        uploadedBy=user3
    )

    sound5 = Sound.objects.create(
        soundID="00005",
        soundFile="BoomNBoard\static\audio\woof.mp3",
        name="woof",
        category="Memes",
        description="Dog woofing a lot.",
        uploadedBy=user2
    )

    SavedSound.objects.create(user=user1, sound=sound2)
    SavedSound.objects.create(user=user1, sound=sound1)
    SavedSound.objects.create(user=user2, sound=sound3)
    SavedSound.objects.create(user=user2, sound=sound4)
    SavedSound.objects.create(user=user3, sound=sound5)

if __name__ == "__main__":
    populate()