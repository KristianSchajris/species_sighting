from django.contrib import admin

from .models import Place, TaxonomicCategory, Specie, Sighting

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name_place', 'country', 'state', 'created_at', 'updated_at')
    ordering     = ('name_place',)

class TaxonomicCategoryAdmin(admin.ModelAdmin):
    list_display = ('kingdom', 'phylum', 't_class', 't_order', 'family', 'genus', 'id_specie', 'created_at', 'updated_at',)
    ordering     = ('kingdom',)

class SpecieAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'scientific_name', 'created_at', 'updated_at',)
    ordering     = ('common_name',)

class SightingAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'latitude', 'longitude', 'notes', 'image_sighting', 'id_place', 'id_specie', 'created_at', 'updated_at')
    ordering     = ('id_user',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(TaxonomicCategory, TaxonomicCategoryAdmin)
admin.site.register(Specie, SpecieAdmin)
admin.site.register(Sighting, SightingAdmin)
