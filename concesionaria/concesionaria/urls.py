from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="API de Concesionaria",
        default_version='v1',
        description="Documentación de la API de Concesionaria",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@concesionaria.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),  # Permitir acceso sin autenticación
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('vehiculos/', include('vehiculos.urls')),
    path('api_v1/', include('api_v1.urls')),

    # Rutas para Swagger y ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
