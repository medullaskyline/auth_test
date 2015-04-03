from django.conf.urls import patterns, url
from bq_app import views

urlpatterns = patterns('',
    url(r'^$', views.bq_home),
)