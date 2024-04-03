from django.test import TestCase
from . import views

# Create your tests here.

class HomeTestCase(TestCase):
    def test_home(self):
        ''' Test the home view '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)