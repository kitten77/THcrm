from user.tests.test_mixing_class import TestUserSetup


class TestUserList(TestUserSetup):

    def test_user_list(self):
        response = self.c.get('/user/list/')
        template_user_list = 'user/user_list.html'
        self.assertTemplateUsed(response=response, template_name=template_user_list)
        self.assertEqual(200, response.status_code)

