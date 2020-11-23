from .base import *

env = environ.Env()

environ.Env.read_env()

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

