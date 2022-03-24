from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from .models import Place
from .serializers import *


class PlaceListView(APIView):

    def get(self, request, format=None):
        places     = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceDetail(APIView):

    def get_object(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        places     = self.get_object(pk)
        serializer = PlaceSerializer(places)

        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
