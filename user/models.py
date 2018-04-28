import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.

# class customUser(AbstractUser):
#     """User model."""
#
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user_uuid = models.UUIDField(null=False, default=uuid.uuid4, editable=False)

    def get_view_url(self):
        """
        returns a reverse url for user view
        """
        return reverse('user:view', kwargs={'user_id': self.user.pk})

    def get_update_url(self):
        """
        returns a reverse url for updating user pk
        """
        return reverse('user:update', kwargs={'user_id': self.user.pk})

    def get_short_name(self):
        return self.user.username

    def get_name(self):
        name = self.user.first_name.title() + ' ' + self.user.last_name.title()
        return name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

### DEPRECATED This only over complicates things
### It is better to leave this alone and go for a onetoone relation for a profile
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', ]
#
#     objects = UserManager()
#
#
#     def __unicode__(self):
#         return self.email
