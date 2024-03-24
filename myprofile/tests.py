from django.test import TestCase

# Create your tests here.


class MyProfileTestCase(TestCase):
    def test_myprofile_not_logged_in(self):
        response = self.client.get('/myprofile/')
        self.assertEqual(response.status_code, 302)
