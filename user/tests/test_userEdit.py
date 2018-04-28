import datetime

from dateutil.relativedelta import relativedelta

from user.tests.test_mixing_class import TestUserSetup


class TestUserEdit(TestUserSetup):
    def test_get(self):
        response = self.c.get(self.user.profile.get_update_url())
        self.assertTemplateUsed(response=response, template_name='user/user_update_form.html')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        birth_date = datetime.datetime.now().date() - relativedelta(years=18)
        user_update = {'first_name': 'test1', 'last_name': 'test1',
                       'email': 'test@test.com', 'username': self.username,
                       'bio': 'this is the bio', 'location': 'Norway',
                       'birth_date': birth_date}
        update_url = self.user.profile.get_update_url()
        response = self.c.post(update_url, user_update, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response=response, template_name='user/user_view.html')
