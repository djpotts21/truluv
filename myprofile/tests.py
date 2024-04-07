from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User

from . import views, models


# Create your tests here.


class MyProfileTestCase(TestCase):
    def test_myprofile(self):
        ''' Test the myprofile view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'GET'
        request.user = User.objects.create_user(username='testuser', password='testpassword')

        # create a profile for the user
        profile = models.Profile(user=request.user)
        profile.save()
        
        # Call the view function
        response = views.myprofile(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 200)

    def test_updatename(self):
        ''' Test the updatename view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        request.POST = {'first_name': 'Test', 'last_name': 'User'}

        # Call the view function
        response = views.updatename(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

    def test_updateusername(self):
        ''' Test the updateusername view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        request.POST = {'username': 'testuser'}

        # Call the view function
        response = views.updateusername(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

    def test_updateaddress(self):
        ''' Test the updateaddress view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a profile for the user
        profile = models.Profile(user=request.user)
        profile.save()
        request.POST = {'address': '123 Test St'}

        # Call the view function
        response = views.updateaddress(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)
    
    def test_updatephone(self):
        ''' Test the updatephone view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a profile for the user
        profile = models.Profile(user=request.user)
        profile.save()
        request.POST = {'phone': '123-456-7890'}

        # Call the view function
        response = views.updatephone(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)
    
    def test_updateage(self):
        ''' Test the updateage view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a profile for the user
        profile = models.Profile(user=request.user)
        profile.save()
        request.POST = {'age': '25'}

        # Call the view function
        response = views.updateage(request)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)
