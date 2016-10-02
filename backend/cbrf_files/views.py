from django.http import HttpResponse
from StringIO import StringIO
from cbrf_files.models import CBRF_Deposit
import os, mimetypes, urllib

def deposits_xml(request):
    header = CBRF_Deposit.objects.order_by('?')[0]
    image = StringIO(file(header.photo.path, "rb").read())
    return HttpResponse(image.read(), content_type='application/xml')
