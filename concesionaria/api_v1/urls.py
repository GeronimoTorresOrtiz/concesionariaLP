from rest_framework.routers import DefaultRouter
from api_v1.views.vehiculos import VehiculoViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, 'vehiculos')

urlpatterns = router.urls