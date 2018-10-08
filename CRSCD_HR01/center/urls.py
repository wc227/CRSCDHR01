from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^resume/$', views.resume),
    url(r'^resume_up/$', views.resume_up),
    url(r'^resume_del/$', views.resume_del),
    url(r'^resume_submit/$', views.resume_submit),
    url(r'^resume_modify', views.resume_modify),
]
