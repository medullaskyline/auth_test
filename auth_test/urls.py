from django.conf.urls import patterns, include, url
from django.contrib import admin
from auth_test import views

urlpatterns = patterns('',
    url(r'^$', views.choose_authentication_system, name="choose_authentication_system"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bq_app/', include('bq_app.urls'))
)
