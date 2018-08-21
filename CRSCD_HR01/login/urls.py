from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login_request),
    url(r'^login_handle/$', views.login_handle),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^center/$', views.center),
]

