from django.utils.deprecation import MiddlewareMixin

from extensions.auth import get_user


class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.xuser = get_user(request)
