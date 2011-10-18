#!/usr/bin/env python
try:
    import django
except ImportError:
    print('''Django is not installed yet.
             Are you running manage.py from within virtualenv?
             Have you run command "pip install -r requirements.txt"?''')
    import sys
    sys.exit(1)

from django.core.management import execute_manager

# if the project directory is not in python path, add it there to be able to import czmag
try:
    import adams_bone_package
except ImportError:
    import sys
    import traceback
    from os.path import dirname, realpath
    source_dir = dirname(dirname(realpath(traceback.extract_stack()[-1][0])))
    sys.stderr.write("Warning: Could not find package 'adams_bone_package' . Inserting directory '%s' to your python path.\n" % source_dir)
    sys.path.insert(0, source_dir)

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
