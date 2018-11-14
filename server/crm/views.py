from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from crm.models import News
from crm.serializers import NewsSerializer
from extensions.auth import login_required
from django.http import JsonResponse
import logging

logger = logging.getLogger('admin_log')


class CrmHome(APIView):
    """后台首页"""

    view_name = 'crm_home'
    template_name = 'crm/index.html'

    @method_decorator(login_required)
    def get(self, request):
        context = dict()
        try:
            print(1 / 0)
        except Exception as error:
            logger.info(error)
        context['user'] = request.xuser
        return render(request, self.template_name, context)


class Sina(APIView):
    """ 微博热搜"""
    view_name = 'sina'
    template_name = 'crm/sina.html'

    @method_decorator(login_required)
    def get(self, request):
        context = dict()
        context['user'] = request.xuser
        return render(request, self.template_name, context)


class SinaList(ListAPIView):
    view_name = 'sina_list'
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-creation_time')


class SinaListBootTable(APIView):
    view_name = 'sina_list_boot_table'
    serializer_class = NewsSerializer

    def get(self, request):
        order = request.query_params.get('order', None)
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 20))

        search = request.query_params.get('search', '').strip()

        qs = News.objects.filter(text__contains=search).order_by('-creation_time')

        ret_data = qs[offset:limit + offset]
        data = self.serializer_class(ret_data, many=True).data

        data = {
            "total": qs.count(),
            "rows": data
        }
        return JsonResponse(data)


class BootTable(APIView):
    """ 微博热搜"""
    view_name = 'boot_table'
    template_name = 'crm/boot_table.html'

    @method_decorator(login_required)
    def get(self, request):
        context = dict()
        context['user'] = request.xuser
        return render(request, self.template_name, context)
