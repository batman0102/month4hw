import time
import logging


class PerformanceLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django.request')

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        self.logger.debug(
            f"Request to {request.path} took {duration:.2f} seconds, Method: {request.method}, Status Code: {response.status_code}")

        return response
