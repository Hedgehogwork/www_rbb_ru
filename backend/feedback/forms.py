from django import forms
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from captcha.fields import CaptchaField

from models import Feedback, Receiver


class FeedbackModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ['theme', 'name', 'email', 'body', 'file1', 'file2', 'file3']

    def send_email(self):
        template_html = 'feedback/new_feedback_email.html'
        template_text = 'feedback/new_feedback_email.txt'
        theme = self.cleaned_data['theme']
        receivers = Receiver.objects.filter(theme=theme).values_list('email', flat=True)
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = u"{0}:{1}".format(theme.name, self.cleaned_data['name'])
        text_content = render_to_string(template_text, {'obj': self.instance})
        html_content = render_to_string(template_html, {'obj': self.instance})
        msg = EmailMultiAlternatives(subject, text_content, from_email, receivers)
        msg.attach_alternative(html_content, "text/html")
        for i in range(1, 4):
            file_object = self.cleaned_data['file1']
            try:
                msg.attach(file_object.name, file_object.read(), file_object.content_type)
            except:
                pass
        msg.send()