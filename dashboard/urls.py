from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^project/$', 'dashboard.project.views.all_projects'),
    url(r'^projects/$', 'dashboard.project.views.all_projects'),
    url(r'^projects/create$', 'dashboard.project.views.create_project'),
    url(r'^project/(?P<project_id>\d+)/$', 'dashboard.project.views.detail'),
    url(r'^project/(?P<project_id>\d+)/analyze/$', 'dashboard.project.views.analyze'),
    url(r'^project/(?P<project_id>\d+)/history/(?P<metric_name>\w+).json', 'dashboard.project.views.history'),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'dashboard.views.view_404'