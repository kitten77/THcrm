from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from common.passwd_gen import passwd_gen


class TestUserSetup(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.login_url = '/user/login/'
        self.password = passwd_gen
        self.new_pass = passwd_gen
        self.username = "l1"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user.save()
        self.c.login(username=self.username, password=self.password)


