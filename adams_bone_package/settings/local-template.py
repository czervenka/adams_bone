import logging
from os.path import join
import sys
from adams_bone_package.settings import PROJECT_ROOT, LOGGING

DEBUG = True
CRON_RUNNER_HOSTNAMES = ('localhost',)
SHOW_DEBUG_TOOLBAR = True
LOGGING['level'] = logging.DEBUG # one of INFO, DEBUG, WARNING, ERROR, CRITICAL, FATAL
LOG_TO_FILE = True # otherwise logs to std error (default)

# DATABASE - default values would probably work perfectly for your developement
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = join(PROJECT_ROOT, 'tmp', 'devel.sqlite3')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


CACHE_BACKEND = "dummy:///"
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
# CACHE_BACKEND = 'locmem://'
SESSION_ENGINE='django.contrib.sessions.backends.file'

# AUTOMATIC SECTION - you will probably never need to change the lines in this section
# LOGGING
if LOG_TO_FILE:
    LOGGING.update({
        'filename': join(PROJECT_ROOT, 'tmp/debug.log'),
        'format': '%(levelname)s\t%(pathname)s:%(lineno)d (%(funcName)s): "\033[33m%(message)s\033[0m"',
    })
else:
    LOGGING.update({
        'filename': None,
        'stream': sys.stderr,
        'format': '%(levelname)s\t%(pathname)s:%(lineno)d (%(funcName)s): "\033[33m%(message)s\033[0m"',
    })

# DEBUG TOOLBAR
if DEBUG and SHOW_DEBUG_TOOLBAR:
    from adams_bone_package.settings.enable_debug_toolbar import *

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    # 'debug_toolbar.panels.sql.SQLDebugPanel',
    # 'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
