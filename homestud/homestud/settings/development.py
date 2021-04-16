from .base import *

# GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal300.dll"

SECRET_KEY = 'ie6b5hb5i#a9@b^6blxx+az(k9ex1x!o7@9cm3i&&#jz_809p@'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    
]

SITE_ID=2

DEBUG = True

PAYSTACK_PUBLIC_KEY = 'pk_test_1301ae5f94c2cf0e0de6689629f73a96b7bfa8bb'
PAYSTACK_SECRET_KEY = 'sk_test_989169108aaf6ab394c715e8db93bba227abcd4d'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = '587'
# EMAIL_HOST_USER = 'appstephen8@gmail.com'
# EMAIL_HOST_PASSWORD = 'scientific'
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Homestud <appstephen8@gmail.com>'


# SERVER_EMAIL = 'admin@homestud.co'
# # admins get notified of errors
# ADMINS = [('Steph', 'noreply.homestud@gmail.com'), ('Admin', 'hello@homestud.co')]

# --------production email settings
# for dkim backend
#EMAIL_BACKEND = 'django_dkim.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'postmaster@sandboxd4e1d6ddb37344329a29f7418eba64b5.mailgun.org'
EMAIL_HOST_PASSWORD = 'e64a7cf9332efdc4f61e58ebc46a30fd-a09d6718-871d216a'
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Homestud <hello@homestud.co>'

SERVER_EMAIL = 'hello@homestud.co'
# admins get notified of errors
ADMINS = [('Steph', 'noreply.homestud@gmail.com')]


SERVER_EMAIL = 'admin@homestud.co'
# admins get notified of errors
ADMINS = [('Steph', 'noreply.homestud@gmail.com'), ('Admin', 'hello@homestud.co')]


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'django_db',
        'USER': 'steph',
        'PASSWORD': 'notreallyscientific4196',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATIC_URL = '/static/'



# mantenance mode settings
MAINTENANCE_MODE = False
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
MAINTENANCE_MODE_TEMPLATE = '503.html'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }
