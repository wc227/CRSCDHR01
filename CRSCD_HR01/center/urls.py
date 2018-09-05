from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^resume/$', views.resume),
    url(r'^photo_upload_handle/$', views.photo_upload_handle),

]