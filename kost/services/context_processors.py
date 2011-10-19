from django.conf import settings
from django.contrib.sites.models import Site

def base_vars(request):
    return {
        'CURRENT_SITE': Site.objects.get_current(),
        'STATIC_URL': settings.STATIC_URL,
    }