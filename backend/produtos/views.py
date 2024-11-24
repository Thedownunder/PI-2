from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Produto
from .serializers import ProdutoSerializer
# Create your views here.

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou editar produtos.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
