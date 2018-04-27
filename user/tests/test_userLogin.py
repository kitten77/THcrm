from user.tests.test_mixing_class import TestUserSetup


class TestUserLogin(TestUserSetup):

    def test_get(self):
        self.c.logout()
        response = self.c.get(self.login_url, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/login.html')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        self.c.logout()
        response = self.c.post(self.login_url, {'username': self.username, 'password': self.password}, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
        self.assertEqual(200, response.status_code)
