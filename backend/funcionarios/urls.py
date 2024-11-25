from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet, ChangePasswordView
from django.urls import path

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)  # Registra a rota 'funcionarios/'

urlpatterns = router.urls

urlpatterns += [
    path('alterar_senha/', ChangePasswordView.as_view(), name='alterar_senha'),
]
