# settings/production.py
from .base import *

SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

ALLOWED_HOSTS = ['.citystories.dk']

CORS_ORIGIN_WHITELIST = (
    'citystories.dk',
    'localhost'
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
