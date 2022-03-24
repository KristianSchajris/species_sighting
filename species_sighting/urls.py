from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/',include('apps.species_sighting_api.routers')),
    url(r'^api/',include('apps.species_sighting_api.routers')),
]

