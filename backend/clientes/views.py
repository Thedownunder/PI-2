from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Cliente
from .serializers import ClienteSerializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou editar clientes.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]  # Requer autenticação para acessar as rotas
