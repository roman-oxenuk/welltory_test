import os
from .common import *


DEBUG = True
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'postgres'),
        'USER': os.environ.get('DJANGO_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        # 'HOST': os.environ.get('DJANGO_DB_HOST', 'db'),
        'HOST': os.environ.get('DJANGO_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }