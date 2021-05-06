from .base import *


SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ["178.62.30.58", ".homestud.co"]

INSTALLED_APPS += [
    'storages',
]

DEBUG = False

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True 
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost'
    }
}

SITE_ID=2
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY')
PAYSTACK_SECRET_KEY = config('PAYSTACK_SECRET_KEY')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_LOCATION = config('AWS_LOCATION') 
AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None

STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# for dkim backend
#EMAIL_BACKEND = 'django_dkim.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.eu.mailgun.org'
EMAIL_PORT = '587'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Homestud <hello@homestud.co>'

SERVER_EMAIL = 'hello@mailgun.homestud.co'
# admins get notified of errors
ADMINS = [('Steph', 'noreply.homestud@gmail.com'), ('Admin', 'christineyawn02@gmail.com')]


# dkim backend settings
# DKIM_SELECTOR = '1611859132.homestud'
# DKIM_DOMAIN = 'homestud.co'
# DKIM_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
# MIICXQIBAAKBgQC8+4DWT81eONsPD9Hv7MOLsUh7oIlPhIczCqv6TPo97Z+8dqpw
# rkelDiG61h/h4vtBGg7d3JqisNrDIdxppGZb8IhdKjFVDj6mky8xbhMTqRHtT20N
# VToKdU6mC3SH8Qpy5yuTTFW+jUyEcjpHm3V4dfFWYVQ1iutA2rWNOWcfewIDAQAB
# AoGBAJQEnVW+rYkGGTXD21gDZunMEoyaIdJBaC+nRSpIDpxguQNBIqAdMQprdinD
# urcPNGI6SbimKAwTX1UE+YFY/b3dhwPmHvdaQ+GQdWKuWqSZAo18V+jatg2p8u5M
# XwGt71Y63cR6GPKWwdoHfKoCyZJIYpI8OtpWs8moh8tCQyORAkEA7pG4gUro+XCf
# bYML8ujfMoEsEYvFKa3gQ6JaxY3cQVuOpBAyDRsyGYgX0H+v80381OuIZ89dK9L3
# E8JcX57DWQJBAMrKS2cHgAyMvF8s8jf0iFIA1KM6jXHbq2YATEEIMIvvPwTXXf74
# kvJzcU7fVf4bPSi3Wiq/XhyLZZlwa+T1AvMCQQDnkp11K0Cv+ClZBO6RUIhvHsGn
# GnQ8u+HH5Q2VW9lju7re+DWNUUu1SsxK/9bMJnR4PVS/56I6CuL41B4UVyipAkBM
# k8+dfGuSUaLgnexpzOGddcrWSMoY8Mbsobgp5pnOfe3iOiG4os162LU0/4lNh6O0
# uGhINDOpu8oGAzn7H7qZAkAULBUJtOb8mYNMCAnT1XO0KJAvbMWBn8596rEFHY9F
# v/LwzIVxW1EFCzGUDJmjtJFcQJAs5NwACGEvbt2sOPP6
# -----END RSA PRIVATE KEY-----'''


BASE_URL = "https://homestud.co"

# error logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# mantenance mode settings
MAINTENANCE_MODE = False
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
MAINTENANCE_MODE_TEMPLATE = '503.html'