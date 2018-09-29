from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class CrmHome(APIView):
    """后台首页"""

    view_name = 'crm_home'
    template_name = 'crm/index.html'

    def get(self, request):
        context = dict()
        return render(request, self.template_name, context)
