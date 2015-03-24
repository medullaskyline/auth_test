from django.conf.urls import patterns, url, include
from allauth import urls

urlpatterns = patterns('',
    url(r'^', include(urls))
)