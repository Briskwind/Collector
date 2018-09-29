from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class Home(APIView):
    """ home page """

    view_name = 'home'
    template_name = 'home/index.html'

    def get(self, request):
        context = dict()
        return render(request, self.template_name, context)


class About(APIView):
    """ about page"""

    view_name = 'about'
    template_name = 'home/about.html'

    def get(self, request):
        context = dict()
        return render(request, self.template_name, context)
