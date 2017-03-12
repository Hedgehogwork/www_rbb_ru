from django import forms
from captcha.fields import CaptchaField
from models import Feddback


class FeedbackModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Feedback
