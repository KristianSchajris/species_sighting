from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'places' ,PlaceViewSet, basename = 'places')
router.register(r'Taxonomic_categories' , TaxonomicCategoryViewSet, basename = 'Taxonomic_categories')
router.register(r'species', SpecieViewSet, basename = 'species')
router.register(r'sightings', SightingViewSet, basename = 'sightings')

urlpatterns = router.urls