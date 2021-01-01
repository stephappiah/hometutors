from .base import *

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal300.dll"

SECRET_KEY = 'ie6b5hb5i#a9@b^6blxx+az(k9ex1x!o7@9cm3i&&#jz_809p@'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

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
