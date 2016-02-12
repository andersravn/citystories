# settings/production.py
from .base import *

SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'

ALLOWED_HOSTS = ['.citystories.dk']

CORS_ORIGIN_WHITELIST = (
    'citystories.dk',
    'localhost:8100'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'citystories',
        'USER': 'super',
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': 'skoer-63.postgres.pythonanywhere-services.com',
        'PORT': '10063',
    }
}

OPBEAT = {
    'ORGANIZATION_ID': get_env_variable('OP_ORGANIZATION_ID'),
    'APP_ID': get_env_variable('OP_APP_ID'),
    'SECRET_TOKEN': get_env_variable('OP_SECRET_TOKEN'),
}
