from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)  # Registra a rota 'produtos/'

urlpatterns = router.urls
