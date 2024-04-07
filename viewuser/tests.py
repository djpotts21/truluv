from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestViewUser(TestCase):
    # Test if the view is accessible with no user id in the URL
    # Expected: 404 as no user 1 will exist in test database
    def test_view_user_no_id(self):
        response = self.client.get(reverse('viewuser', kwargs={'user_id': 1}))
        self.assertEqual(response.status_code, 302)
