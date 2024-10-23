from rest_framework.routers import DefaultRouter
from api_v1.views.vehiculos import VehiculoViewSet

reouter = DefaultRouter()
reouter.register(r'vehiculos', VehiculoViewSet, 'vehiculos')

urlpatterns = reouter.urls