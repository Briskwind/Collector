from django.conf.urls import url

from crm import views

urlpatterns = [
    url(r'^$', views.CrmHome.as_view(), name='crm_home'),
    # url(r'^about/$', views.About.as_view(), name='home'),
]
