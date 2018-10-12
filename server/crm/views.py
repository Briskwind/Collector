from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from extensions.auth import login_required

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
            print(1/0)
        except Exception as error:
            logger.info(error)
        context['user'] = request.xuser
        return render(request, self.template_name, context)
