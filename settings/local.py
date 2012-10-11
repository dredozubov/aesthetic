#flake8: NOQA
try:
    from base import *
except ImportError, e:
    print 'Unable to load base.py:', e

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test_db.sqlite3',                      # Or path to database file if using sqlite3.
        #'USER': '',                      # Not used with sqlite3.
        #'PASSWORD': '',                  # Not used with sqlite3.
        #'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += (
            'debug_toolbar',
        )

INTERNAL_IPS = ('127.0.0.1',)
