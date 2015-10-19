from django.conf.urls import patterns, include, url
from django.contrib import admin
from cars.views import car_home

urlpatterns = patterns('',
    #url(r'^$', 'localmotors.views.home', name='home'),
    url(r'^$', car_home, name='car_home'),
    url(r'^cars/$', car_home, name='car_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('urls_api')),
)
