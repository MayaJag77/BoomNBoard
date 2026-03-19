from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from .models import Sound, AppUser


FAILURE_HEADER = "==================== TEST FAILURE OCCURRED ================================"

# Tests can be run with the command python manage.py test app.tests

class BoomNBoardTests (TestCase):

    # Tests for index.html

    def test_welcome_information(self):
        """
          Tests whether the index.html includes information about the website
         """

        required = "Welcome to BoomNBoard the best place to play your favourite sounds!"
        

        index_response = self.client.get(reverse('index'))

        self.assertEqual(index_response.status_code, 200)
        self.assertContains(index_response, required)

    def tests_buttons_on_index(self):

        """
            Tests whether buttons appear on the homepage
        """
        
        response = self.client.get(reverse('index'))
        html = response.content.decode()

        self.assertIn("RingButton-removebg-preview.png", html)
        self.assertIn("class=\"SoundButton\"", html)

    def tests_audio_on_index(self):

        """
            Tests whether audio is available on the homepage
        """
        
        response = self.client.get(reverse('index'))
        html = response.content.decode()

        self.assertIn("cat.mp3", html)
        self.assertIn("type=\"audio/mpeg\"", html)

    def tests_hearts_and_favourites_on_index(self):

        """
            Tests whether hearts appear on the homepage with ability to favourite
        """
        
        response = self.client.get(reverse('index'))
        html = response.content.decode()

        self.assertIn("LikeButtonWhite.jpg", html)
        self.assertIn("onclick=\"changeImage(this)", html)

    def tests_downloads_on_index(self):

        """
            Tests whether download image appears and has functionality to download on homepage
        """
        
        response = self.client.get(reverse('index'))
        html = response.content.decode()

        self.assertIn("DownloadButton.jpg", html)
        self.assertIn("onclick=\"downloadSong(this)", html)
    
    def tests_sound_names_from_model(self):

        self.user = AppUser.objects.create(
            username="noobmaster69",
            email="NoobTester@test.com",
            password="testPassword"
        )

        self.sound = Sound.objects.create(
              soundID="00002",
              soundFile="media\audio\cat.mp3",
              name="Meow",
              category="Memes",
              description="This is a cat meowing.",
              uploadedBy=self.user
        )

        response = self.client.get(reverse('index'))

        self.assertContains(response, self.sound.name)

    # Tests for categories.html

    def tests_meme_category_title(self):

        """
            Tests if categories.html includes the header memes
        """

        response = self.client.get(reverse('categories'))
        html = response.content.decode()

        self.assertIn("<h2>Memes</h2>", html)

    def tests_ringtones_category_title(self):

        """
            Tests if categories.html includes the header ringtones
        """

        response = self.client.get(reverse('categories'))
        html = response.content.decode()

        self.assertIn(" <h2>Ringtones</h2>", html)

    def tests_music_category_title(self):

        """
            Tests if categories.html includes the header music
        """

        response = self.client.get(reverse('categories'))
        html = response.content.decode()

        self.assertIn(" <h2>Music</h2>", html)

    def tests_hearts_and_favourites_on_categories(self):

        """
            Tests whether hearts appear on the categories page with ability to favourite
        """
        
        response = self.client.get(reverse('categories'))
        html = response.content.decode()

        self.assertIn("LikeButtonWhite.jpg", html)
        self.assertIn("onclick=\"toggleLike(this)", html)

    def tests_buttons_on_categories(self):

        """
            Tests whether buttons appear on the homepage
        """
        
        response = self.client.get(reverse('index'))
        html = response.content.decode()

        self.assertIn("MemeButton-removebg-preview.png", html)

    


