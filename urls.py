from django.conf.urls import patterns, include, url
from .views import index, logout

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^logout/$', logout, name="twenty14.logout")
)
