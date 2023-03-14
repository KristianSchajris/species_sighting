from django.conf.urls  import  url, include
from django.urls       import  re_path
from django.contrib    import  admin

from rest_framework  import  permissions
from drf_yasg.views  import  get_schema_view
from drf_yasg        import  openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Species sighting API",
        default_version='v0.1',
        description="Documentacion del web service para el registro de avistamiento de especies marinas.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cristiancharriscp@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^api/v0.1/',include('apps.species_sighting_api.routers')),
]
