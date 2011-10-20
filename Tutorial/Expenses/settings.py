from constants import *
import os

PROJECT_NAME = 'Expenses'

def absPath(rel):
    return os.path.join(ROOT_PATH, rel)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DB_ENGINE, # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
        'USER': DB_USER,                      # Not used with sqlite3.
        'PASSWORD': DB_PASSWORD,                  # Not used with sqlite3.
        'HOST': DB_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DB_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
ADMIN_MEDIA_PREFIX = '/static/admin/'
ROOT_PATH = os.path.dirname(__file__)
ADMINS = (
    ('Jack Reilly', 'jackdreilly@gmail.com'),
)
MANAGERS = ADMINS
TIME_ZONE = 'America/Los_Angeles'



MEDIA_ROOT = absPath('media')
MEDIA_URL = '/media'
STATIC_URL = '/static'
STATIC_ROOT = absPath('static')


TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
)

# Examples: "http://foo.com/static/admin/", "/static/admin/".
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jke$n#$1c72ex!ykevokt5!i^gn(24n(l647t9=4dnt(vge5*q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    'templates',
)

ROOT_URLCONF = 'Expenses.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'frontend',
    'profiles',
    'registration',
    'expenses',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'expenses.Person'
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/loggedin'
