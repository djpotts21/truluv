from django.test import TestCase
from . import views
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import UserLike


# Create your tests here.
class LikesTestCase(TestCase):
    def test_add_like(self):
        ''' Test the add_like view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'GET'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        user_id = User.objects.create_user(username='testuser2', password='testpassword').id

        # Call the view function
        response = views.add_like(request, user_id)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

    def test_remove_like(self):
        ''' Test the remove_like view '''
        # Create a mock request object
        request = HttpRequest()
        request.method = 'GET'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        object_id = UserLike.objects.create(user=request.user, liked_user=request.user).id

        # Call the view function
        response = views.remove_like(request, object_id)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)
        