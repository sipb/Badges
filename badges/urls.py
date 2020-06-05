from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'badgesapp.views.home', name='home'),
    url(r'^badges/', 'badgesapp.views.badges', name='badges')
)
