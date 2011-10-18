from django.conf import settings
from django.conf.urls.defaults import *

from ella import newman


# Hack to allow Ella to handle default django documentation
# FIXME: Should be set some where else (in Ella?)
from django.contrib import admin
admin.site.root = '/newman/django-admin'

# register ella's admin
newman.autodiscover()

from ella.utils.installedapps import call_modules
call_modules(auto_discover=('register',))

urlpatterns = patterns('', )
# urlpatterns = patterns('',
#     (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
# )

if settings.ENABLE_DEBUG_URLS:
    # only use these urls in DEBUG mode, otherwise they should be handled by your web server
    import django, ella
    from os.path import dirname, join, normpath

    # static files from both admin apps
    DJANGO_ADMIN_ROOT = normpath(join(dirname(django.__file__), 'contrib', 'admin', 'media'))
    ADMIN_ROOTS = (
        normpath(join(dirname(ella.__file__), 'newman', 'media')),
        DJANGO_ADMIN_ROOT,
    )

    # serve static files
    urlpatterns += patterns('',
        # server favicon
        # (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '%s/images/design/favicon.ico' % settings.STATIC_URL.strip('/')}),
        # newman specific files first
        (r'^%s/(?P<path>.*)$' % settings.NEWMAN_MEDIA_PREFIX.strip('/'), 'ella.utils.views.fallback_serve', {'document_roots': ADMIN_ROOTS}),
        # newman specific files first
        (r'^%s/(?P<path>.*)$' % settings.ADMIN_MEDIA_PREFIX.strip('/'), 'django.views.static.serve', {'document_root': DJANGO_ADMIN_ROOT}),
        # rest of the static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^500.html$', 'ella.core.views.handle_error'),
    )

urlpatterns += patterns('',
    # Newman
    (r'^newman/django-admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^newman/', include(newman.site.urls)),
    # (r'^%s/' % 'poll', include('ella.polls.urls')),

    # Ella fallback for everything else
    (r'^', include('ella.core.urls')),
)

handler404 = 'ella.core.views.page_not_found'
handler500 = 'ella.core.views.handle_error'
