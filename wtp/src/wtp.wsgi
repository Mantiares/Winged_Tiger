import os
import sys
sys.path = ['/home/mantiares/Winged_Tiger/wtp/src/wtp'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'wtp.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHander()
