"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from funcionarios.views import CustomTokenObtainPairView, ChangePasswordView
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="PetShop API",
      default_version='v1',
      description="Documentação da API do PetShop",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rotas da API
    path('api/', include('clientes.urls')),
    path('api/', include('dependentes.urls')),
    path('api/', include('pets.urls')),
    path('api/', include('funcionarios.urls')),
    path('api/', include('produtos.urls')),
    path('api/', include('estoque.urls')),
    path('api/', include('vendas.urls')),
    path('api/', include('agendamentos.urls')),
    path('api/funcionarios/', include('funcionarios.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # Autenticação JWT
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/funcionarios/alterar_senha/', ChangePasswordView.as_view(), name='alterar_senha'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Documentação da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

