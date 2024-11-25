from rest_framework.routers import DefaultRouter
from .views import DependenteViewSet

router = DefaultRouter()
router.register(r'dependentes', DependenteViewSet)  # Registra a rota 'dependentes/'

urlpatterns = router.urls
