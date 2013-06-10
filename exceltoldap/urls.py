from django.conf.urls import patterns, include, url

#from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'exceltoldap.views.list_documents', name='list_documents'),
    url(r'^users/$','exceltoldap.views.users', name='users'),
    url(r'^users_soap/$','exceltoldap.views.users_soap', name='users_soap'),
    url(r'^vehicles/$','exceltoldap.views.vehicles', name='vehicles'),
    url(r'^devices/$','exceltoldap.views.devices', name='devices'),
    url(r'^places/$','exceltoldap.views.places', name='places'),
    url(r'^missions/$','exceltoldap.views.missions', name='places'),
    url(r'^all/$','exceltoldap.views.all_items', name='all_items'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)