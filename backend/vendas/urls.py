from rest_framework.routers import DefaultRouter
from .views import VendaViewSet

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)  # Registra a rota 'vendas/'

urlpatterns = router.urls
