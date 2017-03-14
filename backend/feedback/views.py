from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from models import Feedback
from forms import FeedbackModelForm


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackModelForm
    template_name = 'feedback/add.html'

    def get_success_url(self):
        return reverse('feedback-success')
