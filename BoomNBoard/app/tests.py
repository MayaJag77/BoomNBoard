from django.test import TestCase
from django.urls import reverse
from django.conf import settings


FAILURE_HEADER = "==================== TEST FAILURE OCCURRED ================================"

# Tests can be run with the command python manage.py test app.tests

class BoomNBoardTests (TestCase):

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

