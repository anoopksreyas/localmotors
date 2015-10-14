from django.conf.urls import patterns, include, url
from rest_framework import routers

from cars.views import list_cars
router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/list-cars/$', list_cars ,name = 'list_cars_api_endpoint'),
)