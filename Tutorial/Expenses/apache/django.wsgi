import os
import sys 

if path not in sys.path:
    sys.path.insert(0,os.path.join(os.path.dirname(__file__), '..'))
    
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()