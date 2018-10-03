from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView

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
            print('error', error)
            context['message'] = error
            return render(request, self.template_name, context)
        else:

            login(request, user)
            next_url = request.GET.get('next', '/crm/')
            return redirect(next_url)




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
