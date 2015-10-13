from django.conf.urls import patterns, include, url
from django.contrib import admin
from cars.views import carHome

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'localmotors.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', carHome, name='car_home'),
    url(r'^cars/$', carHome, name='car_home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('urls_api')),
)
