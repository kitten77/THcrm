from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from accounts.models import Account
# from contacts.models import Contact
from common.models import Team
from common.utils import CASE_TYPE, PRIORITY_CHOICE, STATUS_CHOICE


class Case(models.Model):
    name = models.CharField(pgettext_lazy("Name of the case", "Name"), max_length=64)
    status = models.CharField(choices=STATUS_CHOICE, max_length=64)
    priority = models.CharField(choices=PRIORITY_CHOICE, max_length=64)
    case_type = models.CharField(choices=CASE_TYPE, max_length=255, blank=True, null=True, default='')
    # account = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    contacts = models.IntegerField()
    # contacts = models.ManyToManyField(Contact)
    closed_on = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    # assigned_to = models.IntegerField()
    assigned_to = models.ManyToManyField(User, related_name='case_assigned_users')
    # teams = models.IntegerField()
    teams = models.ManyToManyField(Team)
    # created_by = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='case_created_by', on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def get_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Meeting", status="Planned")

    def get_completed_meetings(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Meeting").exclude(status="Planned")

    def get_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(content_type=content_type, object_id=self.id, event_type="Task", status="Planned")

    def get_completed_tasks(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Task").exclude(status="Planned")

    def get_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(content_type=content_type, object_id=self.id, event_type="Call", status="Planned")

    def get_completed_calls(self):
        content_type = ContentType.objects.get(app_label="cases", model="case")
        return Event.objects.filter(
            content_type=content_type, object_id=self.id, event_type="Call").exclude(status="Planned")

    def get_assigned_user(self):
        return User.objects.get(id=self.assigned_to.id)
