from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Venda
from .serializers import VendaSerializer
# Create your views here.

class VendaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou registrar vendas.
    """
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
