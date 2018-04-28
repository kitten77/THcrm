from django.test import Client

from user.tests.test_mixing_class import TestUserSetup


class TestUserUpdatePass(TestUserSetup):

    def test_get(self):
        response = self.c.get('/user/change-password/')
        self.assertTemplateUsed(response=response, template_name='user/user_update_pass_form.html')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        new_pass = self.new_pass
        user_update_password = {'old_password': self.password, 'new_password1': 'badpass', 'new_password2': new_pass}
        response = self.c.post('/user/change-password/', user_update_password, follow=True)
        self.assertTemplateUsed(response=response, template_name='user/user_update_pass_form.html')
        user_update_password = {'old_password': self.password, 'new_password1': new_pass, 'new_password2': new_pass}
        response2 = self.c.post('/user/change-password/', user_update_password, follow=True)
        self.assertTemplateUsed(response=response2, template_name='user/user_view.html')
        self.c.logout()
        new_client = Client()
        self.assertTrue(new_client.login(username=self.username, password=new_pass))
        self.assertEqual(200, response.status_code)
