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

# Text to put at the end of each page's <title>.
SITE_TITLE = os.getenv('SITE_TITLE', '')

# Text to put in each page's <h1>.
SITE_HEADER = os.getenv('SITE_HEADER', 'Scout')

# Text to put at the top of the admin index page.
INDEX_TITLE = os.getenv('INDEX_TITLE', '')
