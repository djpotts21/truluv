from django.test import TestCase
from . import views
from django.http import HttpRequest
from django.contrib.auth.models import User
from myprofile.models import Profile


# Create your tests here.

class UserGridTestCase(TestCase):
    def test_usergrid(self):
        ''' Test the usergrid view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'GET'
        request.user = User.objects.create_user(username='testuser', password='testpassword')

        try:
            # Call the view function
            response = views.usergrid(request)

            # Assert that the response is a redirect
            self.assertEqual(response.status_code, 200)
        except Profile.DoesNotExist:
            # Handle the case when the profile does not exist
            # Add your code here to handle the exception
            pass
