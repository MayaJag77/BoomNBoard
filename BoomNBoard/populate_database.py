import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BoomNBoard.settings')
django.setup()

from app.models import Sound, SavedSound, AppUser

def create_user(username, email, password):
    user, created = AppUser.objects.get_or_create(
        username=username,
        email=email
    )
    
    if created:
        user.set_password(password)
        user.save()
    
    return user

def populate():
    AppUser.objects.all().delete()
    Sound.objects.all().delete()
    SavedSound.objects.all().delete()

    user1 = create_user(
        username="karateDog7",
        email="alexKarateLover@test.com",
        password="testPassword"
    )

    user2 = create_user(
        username="noobmaster69",
        email="NoobTester@test.com",
        password="testPassword"
    )

    user3 = create_user(
        username="pterodactyl4",
        email="iLovePterodactyl@test.com",
        password="password12345"
    )

    sound1 = Sound.objects.create(
        soundID="00001",
        soundFile="media\audio\drums.mp3",
        name="Drum",
        category="Music",
        description="Loud Drums",
        uploadedBy=user1
    )

    sound2 = Sound.objects.create(
        soundID="00002",
        soundFile="media\audio\cat.mp3",
        name="Meow",
        category="Memes",
        description="This is a cat meowing.",
        uploadedBy=user2
    )

    sound3 = Sound.objects.create(
        soundID="00003",
        soundFile="media\audio\chatting.mp3",
        name="Yapping",
        category="Memes",
        description="This is someone saying something.",
        uploadedBy=user2
    )

    sound4 = Sound.objects.create(
        soundID="00004",
        soundFile="media\audio\roar.mp3",
        name="Dinosaur Roar",
        category="Memes",
        description="Roar",
        uploadedBy=user3
    )

    sound5 = Sound.objects.create(
        soundID="00005",
        soundFile="media\audio\woof.mp3",
        name="woof",
        category="Memes",
        description="Dog woofing a lot.",
        uploadedBy=user2
    )

    # Saved sounds
    SavedSound.objects.create(appuser=user1, sound=sound2)
    SavedSound.objects.create(appuser=user1, sound=sound1)
    SavedSound.objects.create(appuser=user2, sound=sound3)
    SavedSound.objects.create(appuser=user2, sound=sound4)
    SavedSound.objects.create(appuser=user3, sound=sound5)

    print("Database populated successfully")


if __name__ == "__main__":
    populate()