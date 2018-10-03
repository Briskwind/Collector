from django.utils.deprecation import MiddlewareMixin

from extensions.auth import get_user


class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = get_user(request)