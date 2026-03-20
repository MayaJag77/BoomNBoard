from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from .models import Sound, AppUser, SavedSound
from django.contrib.messages import get_messages


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

    # Tests for help.html

    def test_help_information(self):
        """
          Tests whether the help.html includes helpful information for users
         """

        required_question = "how do I download sounds?"
        required_answer = "Press the download icon"
    
        index_response = self.client.get(reverse('help'))

        self.assertEqual(index_response.status_code, 200)
        self.assertContains(index_response, required_question)
        self.assertContains(index_response, required_answer)

    def test_help_email(self):
        """
          Tests whether the help.html includes an email for users with questions
         """

        required_email = "example@email.com"
    
        index_response = self.client.get(reverse('help'))

        self.assertEqual(index_response.status_code, 200)
        self.assertContains(index_response, required_email)

    def test_help_icons(self):
        """
            Tests if the help.html page includes examples of icons for users to click
        """

        response = self.client.get(reverse('help'))
        html = response.content.decode()

        self.assertIn("LikeButtonWhite.jpg", html)

    # Tests for myaccount.html

    def test_username_displays(self):
        """
            Tests that if a user is logged in, their username displays
        """

        user = AppUser.objects.create_user(
          username="noobmaster69",
          email="NoobTester@test.com",
          password="testPassword"
        )

        self.client.login(username="noobmaster69", password="testPassword")

        response = self.client.get(reverse('myaccount'))
        html = response.content.decode()

        self.assertIn('Hello, noobmaster69!', html)

    def test_upload_sounds_if_logged_in(self):

        """
            Tests that users who are logged in have the ability to click and access files to upload
        """
        user = AppUser.objects.create_user(
          username="noobmaster69",
          email="NoobTester@test.com",
          password="testPassword"
        )

        self.client.login(username="noobmaster69", password="testPassword")

        response = self.client.get(reverse('myaccount'))
        html = response.content.decode()

        self.assertIn("<p>Upload Sound as MP3</p>", html)
        self.assertIn(" onclick=\"document.getElementById('mp3upload').click()", html)

    def tests_uploaded_Sounds(self):

        """
            Tests that users see the text "No sounds uploaded yet!" if they haven't uploaded a sound
        """

        self.user = AppUser.objects.create(
            username="noobmaster69",
            email="NoobTester@test.com",
            password="testPassword"
        )

        self.sound = Sound.objects.create(
        soundID="00001",
        soundFile="media\audio\drums.mp3",
        name="Drum",
        category="Music",
        description="Loud Drums",
        uploadedBy=self.user
    )   
        
        self.user.set_password("testPassword")
        self.user.save()
        self.client.login(username="noobmaster69", password="testPassword")
        
        response = self.client.get(reverse('myaccount'))
        html = response.content.decode()

        self.assertIn("<h2 style=\"text-align: left; font-family: Arial, Helvetica, sans-serif; font-size:30px;\" >Your Uploaded Sounds</h2>", html)
        
        self.assertIn("MusicButton-removebg-preview.png", html)

    def test_favourite_sounds(self):

        """
            Tests that users can see sounds they have favourited in the favourite sounds section
        """

        self.user = AppUser.objects.create(
            username="noobmaster69",
            email="NoobTester@test.com",
            password="testPassword"
        )

        self.sound = Sound.objects.create(
        soundID="00001",
        soundFile="media\audio\drums.mp3",
        name="Drum",
        category="Music",
        description="Loud Drums",
        uploadedBy=self.user
    )   
        
        self.user.set_password("testPassword")
        self.user.save()
        self.client.login(username="noobmaster69", password="testPassword")

        saved = SavedSound.objects.create(appuser=self.user, sound=self.sound)
        
        response = self.client.get(reverse('myaccount'))
        html = response.content.decode()

        self.assertIn("<h2 style=\"text-align: left;\">Favourite Sounds</h2>", html)
        
        self.assertIn("MusicButton-removebg-preview.png", html)


    # Tests for login.html

    def test_successful_login(self):
        """A user should be able to log in"""
        AppUser.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpass123'
        )
        response = self.client.post(reverse('app:login'), {
            'username': 'existinguser',
            'password': 'testpass123',
        })
        self.assertRedirects(response, reverse('app:myaccount'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_login(self):
        """User should not be able to log in with invalid details"""
        response = self.client.post(reverse('app:login'), {
        'username': 'wrong',
        'password': 'wrongpass',
        })
        self.assertRedirects(response, reverse('app:login'))

    def test_empty_field_login(self):
        """User should not be able to log in with empty fields"""
        response = self.client.post(reverse('app:login'), {
        'username': '',
        'password': '',
        })
        self.assertRedirects(response, reverse('app:login'))
    
    def test_error_message_appears(self):
        """An error message should appear if a user provides invalid details"""
        response = self.client.post(reverse('app:login'), {
        'username': 'wrong',
        'password': 'wrongpass',
        }, follow=True)
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid username or password. Try again.")


    # Tests for signup.html

    def test_signup_page_loads(self):
        """Signup page should load successfully"""
        response = self.client.get(reverse('app:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BoomNBoard/signup.html')

    def test_successful_signup(self):
        """A new user can sign up and is redirected to myaccount"""
        response = self.client.post(reverse('app:signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'securepass123',
            'password2': 'securepass123',
        })
        self.assertRedirects(response, reverse('app:myaccount'))
        self.assertTrue(AppUser.objects.filter(username='newuser').exists())

    def test_duplicate_email_redirects_to_login(self):
        """User is redirected to login when email is already registered"""
        AppUser.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpass123'
        )
        response = self.client.post(reverse('app:signup'), {
            'username': 'newuser',
            'email': 'existing@example.com',
            'password1': 'securepass123',
            'password2': 'securepass123',
        })
        self.assertRedirects(response, reverse('app:login'))