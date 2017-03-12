# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatewords
from django.utils.encoding import python_2_unicode_compatible


def update_filename(instance, filename):
    path = "upload/path/"
    format = instance.userid + instance.transaction_uuid + instance.file_extension
    return os.path.join(path, format)


class Receiver(models.Model):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))


class Theme(models.Model):
    name = models.CharField(_('name'), max_length=100)
    receivers = models.ManyToManyField(Receiver)


@python_2_unicode_compatible
class Feedback(models.Model):
    theme = models.ForeignKey(Theme)
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))
    body = models.TextField(_("message"))
    file1 = models.FileField(upload_to=update_filename)
    file2 = models.FileField(upload_to=update_filename)
    file3 = models.FileField(upload_to=update_filename)

    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")

    def __str__(self):
        return truncatewords(self.body, 16)

