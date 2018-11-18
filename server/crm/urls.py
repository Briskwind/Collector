from django.conf.urls import url
from django.views.generic import TemplateView

from crm import views
from extensions.auth import login_required

urlpatterns = [

    # 模版渲染

    url(r'^$', views.CrmHome.as_view(), name='crm_home'),
    # url(r'^about/$', views.About.as_view(), name='home'),

    url(r'^sina', login_required(TemplateView.as_view(template_name="crm/sina.html")), name="sina"),
    url(r'^book/$', login_required(TemplateView.as_view(template_name="crm/book.html")), name="book"),



    # url(r'^candl/$', views.CAndList.as_view(), name="candl"),
    # url(r'^candl_detail/$', views.CAndLDetail.as_view(), name="candl_detail"),
    # url(r'^movies/$', views.Movie.as_view(), name="movie"),

    # api接口
    url(r'^api/sina_list/$', views.SinaList.as_view(), name="api_sina_list"),
    url(r'^api/book_list/$', views.BookList.as_view(), name="api_book_list"),

    # url(r'^api/candl_list/$', views.SinaListBootTable.as_view(), name="api_candl_list"),

    # 其他
    url(r'^boot_table/$', views.BootTable.as_view(), name="boot_table"),
    # url(r'^sina/$', views.Sina.as_view(), name="sina"),
    # url(r'^sina_list/$', views.SinaList.as_view(), name="sina_list"),

]
