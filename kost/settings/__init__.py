"""
Project settings are separated to
base.py  - basic application specific settings
local.py - settings specific to an installation (this should never be saved in repository)
"""
from os.path import dirname, join, exists
import logging
from kost.settings.base import *

PATH = dirname(__file__)
SERVER_CONFIGURATION_FILE = '/etc/kost/conf.py'

# server-specific settings
if exists(SERVER_CONFIGURATION_FILE):
    import imp
    imp.load_source('kost.settings.system', SERVER_CONFIGURATION_FILE)
    from kost.settings.system import *

# finally local settings overides all
# overrides anything
if exists(join(PATH, 'local.py')):
    from kost.settings.local import *

logging.basicConfig(
        **LOGGING
        )

from os import environ
if locals()['HTTP_PROXY'] and 'HTTP_PROXY' not in environ:
    environ['HTTP_PROXY'] = locals()['HTTP_PROXY']
    
