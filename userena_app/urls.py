from django.conf.urls import patterns, url, include
from userena import urls

urlpatterns = patterns('',
    url(r'^', include(urls))
)