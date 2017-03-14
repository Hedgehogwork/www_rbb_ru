from django import forms
from captcha.fields import CaptchaField
from models import Feedback


class FeedbackModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ['theme', 'name', 'email', 'body', 'file1', 'file2', 'file3']
