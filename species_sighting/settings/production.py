import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=['*']))

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': '',
        'OPTIONS': {
            'driver': env.str('DB_DRIVER'),
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
