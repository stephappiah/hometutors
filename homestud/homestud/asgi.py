
import os
import django
from channels.routing import get_default_application
from django.conf import settings


if settings.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.development')
    print('asgi dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.production')

django.setup()
application = get_default_application()
