from django.utils.deprecation import MiddlewareMixin
import logging
from urllib.parse import unquote

mylog = logging.getLogger("django.server")

class LoggingMiddleware(MiddlewareMixin):
    """
    Provides full logging of requests and responses
    """
    _initial_http_body = None

    def process_request(self, request):
        self._initial_http_body = request.body # this requires because for some reasons there is no way to access request.body in the 'process_response' method.
        mylog.info("method: {}. get_full_path: {}, body: {}".format(request.method, request.get_full_path(), unquote(str(self._initial_http_body, 'utf-8')), extra={
            'tags': {
                'url': request.build_absolute_uri()
            }
        }))

    def process_response(self, request, response):
        """
        Adding request and response logging
        """
        # mylog.info("method: {}. get_full_path: {}. body: {} response code: {}. "
        #                    "response "
        #                    "content-length: {}"
        #                    .format(request.method, request.get_full_path(), unquote(str(self._initial_http_body,'utf-8')) ,
        #                            response.status_code,
        #                            len(response.content)), extra={
        #         'tags': {
        #             'url': request.build_absolute_uri()
        #         }
        #     })
        return response


class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("MD2里面的 process_request")
        pass