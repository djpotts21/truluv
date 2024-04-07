from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from myprofile.models import Profile
from . import views


class SendChatTest(TestCase):
    def test_send_chat(self):
        # Create a mock request object
        request = HttpRequest()
        request.method = 'POST'
        request.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create user profile
        profile = Profile(user=request.user)
        profile.save()

        selected_user_id = 1
        request.POST = {'message': 'Hello'}

        # Call the view function
        response = views.send_message(request, selected_user_id)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Assert that the redirect URL is correct
        self.assertEqual(response.url, '/chat/user/1/')