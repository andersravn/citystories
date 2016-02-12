# settings/local.py
from .base import *

SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'andersravn',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

INSTALLED_APPS += ('debug_toolbar',)

OPBEAT = {
    'ORGANIZATION_ID': get_env_variable('OP_ORGANIZATION_ID'),
    'APP_ID': get_env_variable('OP_APP_ID'),
    'SECRET_TOKEN': get_env_variable('OP_SECRET_TOKEN'),
}
