"""
WSGI config for homestud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

# use dev environment if debug is true;
# else prod environment
if settings.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.production')

application = get_wsgi_application()
