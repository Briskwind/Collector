from functools import wraps
from urllib.parse import urlparse

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.middleware.csrf import rotate_token
from django.shortcuts import resolve_url
from django.utils.crypto import constant_time_compare

from home.models import User
from server import settings


def user_passes_test(login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    修改Django 用原本的用户验证方式
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if get_user(request):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator


def login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def get_user(request):
    user = None
    user_id = _get_user_session_key(request)
    print('user_id', user_id)

    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass

    return user


def get_or_create_user(account, password):
    """ 注册时，创建或者返回用户"""
    user = User.objects.filter(account=account).first()

    if user:
        res = user.check_password(password)
        if res:
            return user
        else:
            raise Exception('密码错误')
    else:
        user = User()
        user.account = account
        user.set_password(password)
        user.save()
        return user


LOGUSER_SESSION_KEY = 'user'
HASH_LOGUSER_SESSION_KEY = '_auth_user_hash'


def _get_user_session_key(request):
    # This value in the session is always serialized to a string, so we need
    # to convert it back to Python whenever we access it.

    try:
        return User._meta.pk.to_python(request.session[LOGUSER_SESSION_KEY])
    except KeyError:
        return None


def login(request, user, backend=None):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the user logs in.
    """
    session_auth_hash = ''
    if user is None:
        user = request.loguser
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()

    if LOGUSER_SESSION_KEY in request.session:
        if _get_user_session_key(request) != user.pk or (
                    session_auth_hash and
                    not constant_time_compare(request.session.get(HASH_LOGUSER_SESSION_KEY, ''), session_auth_hash)):
            # To avoid reusing another user's session, create a new, empty
            # session if the existing session corresponds to a different
            # authenticated user.
            request.session.flush()
    else:
        request.session.cycle_key()

    request.session[LOGUSER_SESSION_KEY] = user._meta.pk.value_to_string(user)
    request.session[HASH_LOGUSER_SESSION_KEY] = session_auth_hash
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
