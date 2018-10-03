from django.conf.urls import url

from home import views

# pylint: disable=C0103
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^about/$', views.About.as_view(), name='home'),
    url(r'^user/$', views.UserInfo.as_view(), name='user_info'),

]
