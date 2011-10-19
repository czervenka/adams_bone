'''
Common middleware classes
'''

class SetRemoteAddrFromForwardedFor(object):
    '''
    Handles http-x-forwarded-for header set by NetworkImages proxies.
    '''
    def process_request(self, request):
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            pass
        else:
            # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
            # Take just the first one.
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip


class ExceptionLoggingMiddleware(object):
    '''
    Logs any exception
    '''
    def process_exception(self, request, exception):
        import logging
        import traceback
        logger = logging.getLogger('Exception handler')
        logger.error( traceback.format_exc())
