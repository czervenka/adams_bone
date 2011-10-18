"""
Project settings are separated to
base.py  - basic application specific settings
local.py - settings specific to an installation (this should never be saved in repository)
"""
from os.path import dirname, join, exists
import logging
from adams_bone_package.settings.base import *

PATH = dirname(__file__)
SERVER_CONFIGURATION_FILE = '/etc/adams_bone_package/conf.py'

# server-specific settings
if exists(SERVER_CONFIGURATION_FILE):
    import imp
    imp.load_source('adams_bone_package.settings.system', SERVER_CONFIGURATION_FILE)
    from adams_bone_package.settings.system import *

# finally local settings overides all
# overrides anything
if exists(join(PATH, 'local.py')):
    from adams_bone_package.settings.local import *

logging.basicConfig(
        **LOGGING
        )

from os import environ
if locals()['HTTP_PROXY'] and 'HTTP_PROXY' not in environ:
    environ['HTTP_PROXY'] = locals()['HTTP_PROXY']
    
