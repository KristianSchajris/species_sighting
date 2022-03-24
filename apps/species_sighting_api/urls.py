from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .general_views import *

urlpatterns = [
    url(r'^places', PlaceListView.as_view()),
    url(r'^Place/<int:pk>', PlaceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
