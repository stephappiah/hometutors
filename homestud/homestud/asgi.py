"""
ASGI config for homestud project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.staging')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homestud.settings.production')

application = get_asgi_application()
