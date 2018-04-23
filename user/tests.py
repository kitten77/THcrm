from django.test import TestCase, Client
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import now
from .models import Profile
from common.passwd_gen import passwd_gen

# Create your tests here.
class TestUserProfileModel(TestCase):
    def setUp(self):
        """
        Setting up test for user.model.profile
        """
        self.password = passwd_gen
        self.username = "l1"
        self.email = "l1@tonder.org"
        self.name = "l1_test"

        self.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                    Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. \
                    Sed nisi. Nulla quis sem at nibh elementum imperdiet. \
                    Duis sagittis ipsum. Praesent mauris. \
                    Fusce nec tellus sed augue semper porta. \
                    Mauris massa."
        self.location = "Norway"
        self.birth_date = datetime.datetime.now() - relativedelta(years=18)
        self.c = Client()

        #self.user = User.objects.create(username=self.username, email=self.email, first_name=self.first_name, last_name=self.first_name)
        #self.user.set_password(self.password)
        #self.user.save()
        #self.pk =self.user.pk)
        #profile = Profile.objects.create(user = self.user.pk, bio = self.bio, location=self.location, birth_date=self.birth_date)
        #profile.save()
        #self.profile = Profile.create(bio="")

    # def test_profile_bio(self):
    #     bio = User.objects.get(id=self.user.pk)
    #     self.assertEqual(bio, self.bio)

    def test_create_user(self):
        """
        No login tests
        """
        user_create = {'first_name': self.name, 'last_name': self.name,
                        'email': self.email, 'username': self.username,
                        'form-0-password': self.password, 'form-0-password1': self.password,
                        'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0,
                        'form-MIN_NUM_FORMS': 0, 'form-MAX_NUM_FORMS': 1000,
                        'bio': self.bio, 'location': self.location, 'birth_date': self.birth_date }
        response = self.c.post('/user/create/', user_create, follow=True)
        # print(response.content)
        self.assertEqual(200, response.status_code)

    def test_login_user(self):
        response = self.c.post('/user/login/', {'username': self.username, 'password': self.password}, follow=True)
        self.assertEqual(200, response.status_code)

    def test_list_users(self):
        response = self.c.get('/user/list/')
        self.assertEqual(200, response.status_code)
        
