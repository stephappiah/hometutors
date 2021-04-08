from .base import *

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal300.dll"

SECRET_KEY = 'ie6b5hb5i#a9@b^6blxx+az(k9ex1x!o7@9cm3i&&#jz_809p@'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    
]

SITE_ID=2

PAYSTACK_PUBLIC_KEY = 'pk_test_1301ae5f94c2cf0e0de6689629f73a96b7bfa8bb'
PAYSTACK_SECRET_KEY = 'sk_test_989169108aaf6ab394c715e8db93bba227abcd4d'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'appstephen8@gmail.com'
EMAIL_HOST_PASSWORD = 'scientific'
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Homestud <appstephen8@gmail.com>'


SERVER_EMAIL = 'admin@homestud.co'
# admins get notified of errors
ADMINS = [('Steph', 'noreply.homestud@gmail.com'), ('Admin', 'hello@homestud.co')]


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Dev_2',
        'USER': 'postgres',
        'PASSWORD': 'scientific',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATIC_URL = '/static/'


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
