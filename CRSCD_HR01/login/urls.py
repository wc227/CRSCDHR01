from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),

]

