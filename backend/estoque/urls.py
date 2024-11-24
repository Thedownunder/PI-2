from rest_framework.routers import DefaultRouter
from .views import MovimentacaoEstoqueViewSet

router = DefaultRouter()
router.register(r'estoque', MovimentacaoEstoqueViewSet)  # Registra a rota 'estoque/'

urlpatterns = router.urls
