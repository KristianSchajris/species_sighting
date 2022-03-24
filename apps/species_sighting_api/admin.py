from django.contrib import admin

from .models import *

admin.site.register(Place)
admin.site.register(TaxonomicCategory)
admin.site.register(Specie)
admin.site.register(Sighting)
