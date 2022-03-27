from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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
    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['pk_specie']


# class based views.GenericAPIView for CRUD operations on the model Sighting with the serializer SightingSerializer
# class SightingViewSet(viewsets.GenericAPIView):
#     serializer_class = SightingSerializer
#     queryset         = Sighting.objects.all()
#     lookup_field     = 'pk'

#     def get_object(self):
#         pk = self.kwargs.get(self.lookup_field)
#         return get_object_or_404(Sighting, pk=pk)

#     def get(self, request, *args, **kwargs):
#         sighting = self.get_object()
#         serializer = self.get_serializer(sighting)
#         return Response(serializer.data)

#     def put(self, request, *args, **kwargs):
#         sighting = self.get_object()
#         serializer = self.get_serializer(sighting, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     def delete(self, request, *args, **kwargs):
#         sighting = self.get_object()
#         self.perform_destroy(sighting)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_update(self, serializer):
#         serializer.save()

#     def perform_destroy(self, instance):
#         instance.delete()
