from django.contrib.auth.models import User
from django.test import TestCase, Client

from common.passwd_gen import passwd_gen


class TestUserCreate(TestCase):

    def setUp(self):
        self.password = passwd_gen
        self.username = "l1"
        self.email = "l1@tonder.org"
        self.name = "l1_test"
        self.c = Client()

    def test_get(self):
        """
        No login tests
        """
        response = self.c.get('/user/create/', follow=True)
        self.assertTemplateUsed(response=response, template_name='user/user_create_form.html')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        user_create = {'first_name': self.name, 'last_name': self.name,
                        'email': self.email, 'username': self.username,
                        'form-0-password': self.password, 'form-0-password1': self.password,
                        'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0,
                        'form-MIN_NUM_FORMS': 0, 'form-MAX_NUM_FORMS': 1000, }
        response = self.c.post('/user/create/', user_create, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
        self.assertEqual(200, response.status_code)
        user = User.objects.get(username=self.username)
        entry = user.profile.get_name()
        name = self.name.title() + ' ' + self.name.title()
        self.assertEqual(entry, name)

