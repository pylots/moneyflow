from django.db import models

# Create your models here.
import uuid

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class EventQuerySet(models.QuerySet):

    def created_by(self, user):
        return self.filter(created_by=user)

    def accepted_by(self, user):
        return self.filter(body__accepter=user.email)


# Create your models here.


class BaseEvent(models.Model):
    id = models.BigAutoField(_('Internal ID'), primary_key=True, editable=False)
    version = models.IntegerField(_('Event Version'), default=1, editable=False)
    event = models.CharField(_('Event'), max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    body = JSONField(_('Body'))

    class Meta:
        abstract = True
        ordering = ['id']

    objects = EventQuerySet.as_manager()
