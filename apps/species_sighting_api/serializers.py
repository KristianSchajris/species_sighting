from django.forms import ValidationError
from rest_framework import serializers

from .models import *


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class TaxonomicCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaxonomicCategory
        fields = '__all__'


class SpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specie
        fields = '__all__'


class SightingSerializer(serializers.Serializer):

    class Meta:
        model = Sighting
        fields = '__all__'

