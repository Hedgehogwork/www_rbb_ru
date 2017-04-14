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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(FeedbackCreate, self).form_valid(form)
