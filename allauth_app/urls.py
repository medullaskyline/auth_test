from django.conf.urls import patterns, url, include
from allauth import urls
from allauth_app import views

urlpatterns = patterns('',
    url(r'^', include(urls)),
    url(r'^$', views.allauth_profiles)
)