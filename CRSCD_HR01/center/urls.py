from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^resume/$', views.resume),
    url(r'^resume_up/$', views.resume_up),
    url(r'^resume_del/$', views.resume_del),
    url(r'^resume_submit/$', views.resume_submit),
    url(r'^resume_modify/$', views.resume_modify),
    url(r'^work_del/$', views.work_del),
    url(r'^edu_del/$', views.edu_del),
    url(r'^postView/$', views.post_view),
    url(r'^postModal/$', views.post_modal),
]
