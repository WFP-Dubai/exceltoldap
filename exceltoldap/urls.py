from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'exceltoldap.views.home', name='home'),
    url(r'^list/$', 'exceltoldap.views.list', name='list'),
    url(r'^users/$','exceltoldap.views.users', name='users'),
    url(r'^vehicles/$','exceltoldap.views.vehicles', name='vehicles'),
    url(r'^places/$','exceltoldap.views.places', name='places'),
    url(r'^all/$','exceltoldap.views.all_items', name='all_items'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)