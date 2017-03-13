from django import forms
from captcha.fields import CaptchaField
from models import Feedback


class FeedbackModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ['pub_date', 'headline', 'content', 'reporter']

    theme = models.ForeignKey(Theme)
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))
    body = models.TextField(_("message"))
    file1 = models.FileField(upload_to=update_filename, null=True, blank=True)
    file2 = models.FileField(upload_to=update_filename, null=True, blank=True)
    file3 = models.FileField(upload_to=update_filename, null=True, blank=True)
