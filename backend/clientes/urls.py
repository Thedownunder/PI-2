from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)  # Registra a rota 'clientes/'

urlpatterns = router.urls
