from asyncore                   import  read
from django.forms               import  ValidationError
from rest_framework             import  serializers
from django.contrib.auth.models import  User

from .models import *

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model  = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)
    
    def to_representation(self, instance):
        return {
            'id'         : instance.id,
            'username'   : instance.username,
            'first_name' : instance.first_name,
            'last_name'  : instance.last_name,
            'email'      : instance.email,
        }


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Place
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        return {
            'id'         : instance.id,
            'name_place' : instance.name_place,
            'country'    : instance.country,
            'state'      : instance.state,
        }


class TaxonomicCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = TaxonomicCategory
        exclude = ('created_at', 'updated_at', 'id_specie',)
    
    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'kingdom'   : instance.kingdom,
            'phylum'    : instance.phylum,
            't_class'   : instance.t_class,
            't_order'   : instance.t_order,
            'family'    : instance.family,
            'genus'     : instance.genus,
        }


class SpecieSerializer(serializers.ModelSerializer):
    taxonomic_category = TaxonomicCategorySerializer(required=True)

    class Meta:
        model   = Specie
        exclude = ('created_at', 'updated_at')

    def create(self, validated_data):
        taxonomic_category              = validated_data.pop('taxonomic_category')
        specie                          = Specie.objects.create(**validated_data)
        taxonomic_category['id_specie'] = specie

        TaxonomicCategory.objects.create(**taxonomic_category)

        return specie
    
    def __search_taxonomic_category(self, id_specie):
        taxonomic_category = TaxonomicCategory.objects.filter(id_specie=id_specie)
        
        return taxonomic_category
    
    def to_representation(self, instance):
        taxonomic_category = self.__search_taxonomic_category(instance.id)

        return {
            'id'              : instance.id,
            'common_name'     : instance.common_name,
            'scientific_name' : instance.scientific_name,
            'taxonomic_category' : {
                'kindom'          : taxonomic_category[0].kingdom,
                'phylum'          : taxonomic_category[0].phylum,
                't_class'         : taxonomic_category[0].t_class,
                't_order'         : taxonomic_category[0].t_order,
                'family'          : taxonomic_category[0].family,
                'genus'           : taxonomic_category[0].genus,
            }
        }


class SightingSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Sighting
        exclude = ('created_at', 'updated_at')
    
    def to_representation(self, instance):
        return {
            'id'             : instance.id,
            'author'         : AuthorSerializer(instance.id_user).data,
            'latitude'       : instance.latitude,
            'longitude'      : instance.longitude,
            'image_sighting' : (instance.image_sighting == None) if instance.image_sighting else '',
            'notes'          : instance.notes,
            'specie'         : SpecieSerializer(instance.id_specie).data,
            'place'          : PlaceSerializer(instance.id_place).data,
            'created_at'     : instance.created_at,
        }
