import datetime
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView

from crm.models import Book
from crm.serializers import BookSerializer
from extensions.auth import get_or_create_user, login
from extensions.sqlite_conn import get_one_user


class Home(APIView):
    """ home page """

    view_name = 'home'
    template_name = 'home/index.html'

    def get(self, request):
        context = dict()
        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        account = strip_tags(request.POST.get('username', '').strip())
        password = strip_tags(request.POST.get('password', '').strip())

        context = {}

        try:
            user = get_or_create_user(account=account, password=password)
        except Exception as error:
            context['message'] = error
            return render(request, self.template_name, context)
        else:

            login(request, user)
            max_age = 1 * 3600

            request.session.set_expiry(max_age)


            next_url = request.GET.get('next', '/crm/')
            return redirect(next_url)


class LoginOut(APIView):
    """ 退出登陆"""

    def get(self, request):
        request.session.flush()
        return HttpResponseRedirect('/')


class About(APIView):
    """ about page"""

    view_name = 'about'
    template_name = 'home/about.html'

    def get(self, request):
        context = dict()
        return render(request, self.template_name, context)


class UserInfo(APIView):
    """ sql 注入测试"""

    def get(self, request):
        user_id = request.query_params.get('user_id', 1)
        res = get_one_user(user_id)

        return HttpResponse(res)



class JsonP(APIView):
    """ JsonP test"""

    serializer_class = BookSerializer

    def get(self, request):
        func = request.GET.get("func")

        qs = Book.objects.filter()

        res = self.serializer_class(qs, many=True).data

        data = {
            "total": qs.count(),
            "rows": res
        }


        return HttpResponse('callback("{0}")'.format(data))