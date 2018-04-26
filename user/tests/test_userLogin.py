from django.contrib.auth.models import User
from django.test import TestCase, Client

from common.passwd_gen import passwd_gen


class TestUserLogin(TestCase):

    def setUp(self):
        self.c = Client()
        self.url = '/user/login/'
        self.password = passwd_gen
        self.username = "l1"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_get(self):
        response = self.c.get(self.url, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/login.html')

    def test_post(self):
        response = self.c.post(self.url, {'username': self.username, 'password': self.password}, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
        self.assertEqual(200, response.status_code)
