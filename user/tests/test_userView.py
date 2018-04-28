from user.tests.test_mixing_class import TestUserSetup


class TestUserView(TestUserSetup):

    def test_get(self):
        response = self.c.get(self.user.profile.get_view_url())
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
        self.assertEqual(200, response.status_code)
        response = self.c.get('/user/me/')
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
        self.assertEqual(200, response.status_code)
