# https://www.coderedcorp.com/blog/django-settings-for-multiple-environments/
# python manage.py runserver --settings=BackendDev.testSettings
from BackendDev.settings import *

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : BASE_DIR / 'databases' / 'testing.sqlite3'
    }
}