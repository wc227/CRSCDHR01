from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^logIn/$', views.log_in),
    url(r'^logOut/$', views.log_out),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^loginHandle/$', views.login_handle),
    url(r'^changePassword/$', views.change_pwd),
]


