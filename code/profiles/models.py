import uuid

from django.conf import settings
from django.db import models


class BaseProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE
    )
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    email_verified = models.BooleanField("Email verified", default=False)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class Profile(BaseProfile):

    def __str__(self):
        return "{}'s profile".format(self.user)
