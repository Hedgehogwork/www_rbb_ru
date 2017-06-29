# -*- coding: utf-8 -*-
import os
import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatewords
from django.utils.encoding import python_2_unicode_compatible


def update_filename(instance, filename):
    path = "upload/path/"
    ext = filename.rsplit('.')[1]
    fn = unicode(uuid.uuid4())
    return "{0}/{1}.{2}".format(path, fn, ext)


class Receiver(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))

    def __unicode__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(_('name'), max_length=100)
    receivers = models.ManyToManyField(Receiver)

    def __unicode__(self):
        return self.name


@python_2_unicode_compatible
class Feedback(models.Model):
    theme = models.ForeignKey(Theme)
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))
    body = models.TextField(_("message"))
    file1 = models.FileField(upload_to=update_filename, null=True, blank=True)
    file2 = models.FileField(upload_to=update_filename, null=True, blank=True)
    file3 = models.FileField(upload_to=update_filename, null=True, blank=True)
    ip = models.CharField(max_length=50, null=True, blank=True)
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")

    def __str__(self):
        return truncatewords(self.body, 16)

    def __unicode__(self):
        return truncatewords(self.body, 16)
