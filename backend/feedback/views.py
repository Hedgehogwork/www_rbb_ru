from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from models import Feedback
from forms import FeedbackModelForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackModelForm
    template_name = 'feedback/add.html'

    def get_success_url(self):
        return reverse('feedback-success')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.ip = get_client_ip(self.request)
        form.send_email()
        return super(FeedbackCreate, self).form_valid(form)
