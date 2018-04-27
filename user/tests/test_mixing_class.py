from django.contrib.auth.models import User
from django.test import TestCase, Client

from common.passwd_gen import passwd_gen


class TestUserSetup(TestCase):

    def setUp(self):
        self.c = Client()
        self.login_url = '/user/login/'
        self.password = passwd_gen
        self.username = "l1"
        self.user = User.objects.create_user(username=self.username, password=self.password)