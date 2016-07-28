import os, sys
sys.path.append('/bhome/part3/03/vh47992/new.rbb.ru_django/backend')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()