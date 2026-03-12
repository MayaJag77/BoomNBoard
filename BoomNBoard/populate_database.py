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

    sound1 = Sound.objects.create(
        soundID="00001",
        soundFile="https://test.com/sounds/drum.mp3",
        name="Drum",
        category="Music",
        description="Loud Drums",
        uploadedBy=user1
    )

    sound2 = Sound.objects.create(
        soundID="00002",
        soundFile="https://test.com/sounds/meow.mp3",
        name="Meow",
        category="Memes",
        description="This is a cat meowing.",
        uploadedBy=user2
    )

    SavedSound.objects.create(user=user1, sound=sound2)
    SavedSound.objects.create(user=user1, sound=sound1)

if __name__ == "__main__":
    populate()