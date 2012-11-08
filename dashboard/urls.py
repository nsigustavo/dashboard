from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^project/(?P<project_id>\d+)/$', 'dashboard.project.views.detail'),
    url(r'^project/(?P<project_id>\d+)/analyze/$', 'dashboard.project.views.analyze'),
    url(r'^project/(?P<project_id>\d+)/(?P<task>\w+)/$', 'dashboard.project.views.run_task', name='run_task'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/$', 'dashboard.project.views.all_projects'),
)

handler404 = 'dashboard.views.view_404'
