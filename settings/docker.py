import os
from .common import *


DEBUG = False
if os.getenv('DEBUG', 'false').lower() in ('true', 'yes'):
    DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'postgres'),
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.getenv('DATABASE_HOST', 'db'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    },
}

MEDIA_ROOT = '/media'
STATIC_ROOT = '/static'
