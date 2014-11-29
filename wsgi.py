import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler

# set application for WSGI processing
application = WSGIHandler()
