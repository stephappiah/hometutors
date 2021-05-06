
import os
from pathlib import Path
from decouple import config
 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


INSTALLED_APPS = [
    'admin_interface',
    'colorfield',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    
    'maintenance_mode',

    'django.contrib.gis',
    'multiselectfield',
    'formtools',
    'crispy_forms',
    'bootstrap4',
    'phonenumber_field',
    'bootstrap_datepicker_plus',
    'channels',

    'users',
    'payments',
    'findtutors',
    'groupstudy',
    'chat',
    'star_ratings',
    'django_q',

    'admin_honeypot',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter', 
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# below for bootsttrap_datepicker_plus
BOOTSTRAP4 = {
    'include_jquery': True,
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
# ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

SOCIALACCOUNT_ADAPTER = 'users.adapter.MySocialAccountAdapter'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = { 
    
    'signup': 'users.forms.CustomSignupForm', 
} 

SOCIALACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSocialSignupForm'
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# set rating stars size in frontend
STAR_RATINGS_STAR_HEIGHT = 18

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'homestud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'maintenance_mode.context_processors.maintenance_mode',
            ],
        },
    },
]



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',   
]

AUTH_USER_MODEL = 'users.User'

ASGI_APPLICATION = 'homestud.routing.application'

WSGI_APPLICATION = 'homestud.wsgi.application'


CHANNEL_LAYERS = {
  'default': {
      'BACKEND': 'channels_redis.core.RedisChannelLayer',
      'CONFIG': {
        'hosts': [('localhost', 6379)],
      },
  },
}


# django q stuff
Q_CLUSTER = {
    'name': 'homestud',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'ack_failures': True,
    'max_attempts': 1,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0, 
        }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, '/groupstudy/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')
MEDIA_URL = '/img/'

