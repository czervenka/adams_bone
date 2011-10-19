# Django settings for kost project.

import logging
from os.path import join, dirname
PROJECT_ROOT = dirname(dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = True
HTTP_PROXY = None

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

DATE_FORMAT = 'd.m.Y'

DATETIME_FORMAT = '%s %s' % (DATE_FORMAT, 'H:i')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(PROJECT_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'
NEWMAN_MEDIA_PREFIX = MEDIA_URL + 'newman/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

SESSION_ENGINE='django.contrib.sessions.backends.cached_db'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-njg3qwi1ix)(!6)=fuqv$8ca)k-3scla@7%u+kd#6(murk5-s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'kost.services.middleware.ExceptionLoggingMiddleware',
    'kost.services.middleware.SetRemoteAddrFromForwardedFor',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'ella.core.middleware.DoubleRenderMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'kost.urls'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'ella.newman.context_processors.newman_media',
    'kost.services.context_processors.base_vars',
)

DEFAULT_MARKUP = 'markdown'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',

    'django.contrib.redirects',
    'tagging',
    'ella.core',
    'ella.newman',
    'ella.newman.licenses',
    'ella.photos',
    'ella.articles',
    'ella.galleries',
    'ella.positions',
    'ella.ellatagging',

    'djangomarkup',
    'kost.services',
)

DOUBLE_RENDER = False

PERSISTENT_STORAGE_BACKEND = 'db://data_cache'

LOGIN_URL = '/ucty/prihlaseni'
LOGOUT_URL = '/ucty/odhlaseni'
ACCOUNT_URL = '/ucty/profil'
LOGIN_REDIRECT_URL = '/ucty/profil'

CRON_RUNNER_HOSTNAMES = ('localhost',)

LOGGING = {
    'filename': '/var/log/kost.log',
    'level': logging.WARNING,
    'version': 1,
}
