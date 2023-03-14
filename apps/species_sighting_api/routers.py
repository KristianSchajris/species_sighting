from rest_framework.routers import DefaultRouter


from .views.place_view import PlaceViewSet
from .views.taxonomic_category_view import TaxonomicCategoryViewSet
from .views.specie_view import SpecieViewSet
from .views.sighting_view import SightingViewSet

router = DefaultRouter()

router.register(r'places' ,PlaceViewSet, basename = 'places')
router.register(r'Taxonomic_categories' , TaxonomicCategoryViewSet, basename = 'Taxonomic_categories')
router.register(r'species', SpecieViewSet, basename = 'species')
router.register(r'sightings', SightingViewSet, basename = 'sightings')

urlpatterns = router.urls
