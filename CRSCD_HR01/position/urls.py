from django.conf.urls import url
from position import views


urlpatterns = [
    url(r'^postHandle/$', views.position_handle),
    url(r'^schoolPosition/$', views.school_position),
    url(r'^generalPosition/$', views.general_position),
    url('^PositionSearch/$', views.PositionSearchView.as_view(), name='haystack_search'),
]
