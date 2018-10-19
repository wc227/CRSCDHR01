from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^postHandle/$', views.post_handle),
    url(r'^schoolPosition/$', views.school_position),
    url(r'^generalPosition/$', views.general_position),

]