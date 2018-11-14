from django.conf.urls import url
from django.views.generic import TemplateView

from crm import views

urlpatterns = [
    url(r'^$', views.CrmHome.as_view(), name='crm_home'),
    # url(r'^sina', TemplateView.as_view(template_name="crm/sina.html"),name="sina"),
    url(r'^sina/$', views.Sina.as_view(),name="sina"),
    url(r'^sina_list/$', views.SinaList.as_view(), name="sina_list"),
    url(r'^api/sina_list_boot_table/$', views.SinaListBootTable.as_view(), name="sina_list_boot_table"),

    url(r'^boot_table/$', views.BootTable.as_view(), name="boot_table"),

    # url(r'^about/$', views.About.as_view(), name='home'),
]
