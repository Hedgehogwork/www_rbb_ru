from django.conf.urls import url
from views import FeedbackCreate
from django.views.generic import TemplateView


urlpatterns = [
    url(r'add/$', FeedbackCreate.as_view(), name='feedback-add'),
    url(r'^success/$', TemplateView.as_view(template_name="feedback/success.html"), name='feedback-success'),
]