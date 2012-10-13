from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^project/(?P<project_id>\d+)/$', 'dashboard.project.views.detail'),
    url(r'^project/(?P<project_id>\d+)/analyse/$', 'dashboard.project.views.analyse'),
    url(r'^admin/', include(admin.site.urls)),
)
