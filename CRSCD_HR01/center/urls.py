from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^resume_create/$', views.resume_create),
    url(r'^resume_up/$', views.resume_up),
    url(r'^resume_del$', views.resume_del),
]