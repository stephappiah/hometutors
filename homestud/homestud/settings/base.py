
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env(env_file='.env')

root = environ.Path(__file__)

public_root = root.path('public/')

GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal300.dll"

BASE_DIR = root()


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
 
    'django.contrib.gis',
    'multiselectfield',
    'formtools',
    'crispy_forms',
    'phonenumber_field',
    'channels',

    'users',
    'findtutors',

    'django_chatter',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter', 
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

LOGIN_REDIRECT_URL = '/'
ACCOUNT_FORMS = { 
    
    'signup': 'users.forms.CustomSignupForm', 
} 


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'homestud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [public_root('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
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
        'hosts': [('127.0.0.1', 6379)],
      },
  },
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    public_root('static')
]

MEDIA_ROOT = public_root('static/img')
MEDIA_URL = '/images/'
