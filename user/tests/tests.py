# import datetime
#
# from dateutil.relativedelta import relativedelta
# from django.test import TestCase, Client
#
# from common.passwd_gen import passwd_gen
#
#
# # Create your tests here.
# class TestUserProfileModel(TestCase):
#     def setUp(self):
#         """
#         Setting up test for user.model.profile
#         """
#         self.password = passwd_gen
#         self.username = "l1"
#         self.email = "l1@tonder.org"
#         self.name = "l1_test"
#
#         self.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
#                     Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. \
#                     Sed nisi. Nulla quis sem at nibh elementum imperdiet. \
#                     Duis sagittis ipsum. Praesent mauris. \
#                     Fusce nec tellus sed augue semper porta. \
#                     Mauris massa."
#         self.location = "Norway"
#         self.birth_date = datetime.datetime.now() - relativedelta(years=18)
#         user_update = {'first_name': self.name, 'last_name': self.name,
#                        'email': self.email, 'username': self.username,
#                        'bio': self.bio, 'location':self.location,
#                        'birth_date': self.birth_date}
#
#         user_create = {'first_name': self.name, 'last_name': self.name,
#                        'email': self.email, 'username': self.username,
#                        'form-0-password': self.password, 'form-0-password1': self.password,
#                        'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0,
#                        'form-MIN_NUM_FORMS': 0, 'form-MAX_NUM_FORMS': 1000, }
#
#         self.c = Client()
#
#     def test_create_user(self):
#         """
#         No login tests
#         """
#         user_create = {'first_name': self.name, 'last_name': self.name,
#                         'email': self.email, 'username': self.username,
#                         'form-0-password': self.password, 'form-0-password1': self.password,
#                         'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0,
#                         'form-MIN_NUM_FORMS': 0, 'form-MAX_NUM_FORMS': 1000, }
#         response = self.c.post('/user/create/', user_create, follow=True)
#         # print(response.content)
#         self.assertEqual(200, response.status_code)
#
#     def test_update_user(self):
#         """
#         Login as user and update profile
#         """
#
#         user = User.objects.create_user(self.username, self.email, self.password)
#         self.c.login(username=self.username, password=self.password)
#         print(user.profile.get_view_url)
#         # self.test_create_user()
#         # self.c.login(email=self.email, password=self.password)
#         user_update = {'first_name': self.name, 'last_name': self.name,
#                        'email': self.email, 'username': self.username,
#                        'bio': self.bio, 'location':self.location,
#                        'birth_date': self.birth_date }
#         update_url = user.profile.get_update_url()
#         response = self.c.post(update_url, user_update, follow=True)
#         entry = user.profile.bio
#         self.assertEqual(entry, self.bio)
#         self.assertEqual(200, response.status_code)
#         return user
#
#     def test_login_user(self):
#         response = self.c.post('/user/login/', {'username': self.username, 'password': self.password}, follow=True)
#         self.assertEqual(200, response.status_code)
#
#     def test_list_users(self):
#         response = self.c.get('/user/list/')
#         template_user_list = 'user/user_list.html'
#         self.assertTemplateUsed(response=response, template_name=template_user_list)
#         self.assertEqual(200, response.status_code)
#
#     def test_create_user_link(self):
#         response = self.c.get('/user/create/')
#         self.assertEqual(200, response.status_code)
#
#     def test_user_name(self):
#         self.test_create_user()
#         user = User.objects.get(username=self.username)
#         entry = user.profile.get_name()
#         name = self.name.title() + ' ' + self.name.title()
#         self.assertEqual(entry, name)
