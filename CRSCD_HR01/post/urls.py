from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^postView/$', views.post_view),
]