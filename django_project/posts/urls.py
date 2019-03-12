from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #  path('^$', views.index, name='index')
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
