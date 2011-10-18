import logging
from adams_bone_package.settings.base import INSTALLED_APPS, MIDDLEWARE_CLASSES
try:
    import debug_toolbar
except ImportError, e:
    logging.error('''You have enabled debug toolbar which is not installed.
    You need to install django-debug-toolbar (http://pypi.python.org/pypi/django-debug-toolbar/0.8.4) by running pip install django-debug-toolbar.
    Shell I install it for you? [Y,n]
    ''')
    c = None
    while c not in ('y','n','a',):
        c = raw_input().strip().lower()
        if c in ('y','a', ''):
            print 'Yes: Initializing automatic installation.'
            import pip
            try:
                pip.main(initial_args=['install', 'django-debug-toolbar',])
            except SystemExit:
                print 'Done. Continuing manage command.'
                break
        elif c == 'n':
            print 'No: Ok, as you wish.'
        else:
            print 'What? [Y,n]'
        

