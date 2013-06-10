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
    url(r'^vehicles_soap/$','exceltoldap.views.vehicles_soap', name='vehicles_soap'),
    url(r'^devices/$','exceltoldap.views.devices', name='devices'),
    url(r'^devices_soap/$','exceltoldap.views.devices_soap', name='devices_soap'),
    url(r'^places/$','exceltoldap.views.places', name='places'),
    url(r'^places_soap/$','exceltoldap.views.places_soap', name='places_soap'),
    url(r'^missions/$','exceltoldap.views.missions', name='places'),
    url(r'^missions_soap/$','exceltoldap.views.missions_soap', name='places_soap'),
    url(r'^all/$','exceltoldap.views.all_items', name='all_items'),
    url(r'^all_soap/$','exceltoldap.views.all_items_soap', name='all_items_soap'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)