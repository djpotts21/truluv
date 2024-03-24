from django.test import TestCase

# Create your tests here.

class MyProfileTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/myprofile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Profile')
        self.assertTemplateUsed(response, 'myprofile/profile.html')


    def test_not_logged_in(self):
        response = self.client.get('/myprofile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/myprofile/')

    def test_logged_in(self):
        self.client.login(username='testuser', password='123ABC45')
        response = self.client.get('/myprofile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Profile')
        self.assertTemplateUsed(response, 'myprofile/profile.html')