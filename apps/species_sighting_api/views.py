from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset         = Place.objects.all()


class TaxonomicCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = TaxonomicCategorySerializer
    queryset         = TaxonomicCategory.objects.all()

class SpecieViewSet(viewsets.ModelViewSet):
    serializer_class = SpecieSerializer
    queryset         = Specie.objects.all()

class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    queryset         = Sighting.objects.all()

    # servicio adicional para la consulta de avistamientos por especie.
    # http://localhost:8000/api/sightings/?pk_specie=<int:pk_specie>
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pk_specie']


