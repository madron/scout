import os
from .default import *


INSTALLED_APPS = [
    'authentication',
    'clothes',
    'reversion',
    'material',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')
