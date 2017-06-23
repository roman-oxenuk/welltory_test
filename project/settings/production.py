import os
from .common import *


MEDIA_ROOT = os.path.join(BASE_DIR, '..', STATIC_FOLDER, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'welltory_test',
    }
}
