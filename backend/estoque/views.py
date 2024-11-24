from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import MovimentacaoEstoque
from .serializers import MovimentacaoEstoqueSerializer
# Create your views here.

class MovimentacaoEstoqueViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou registrar movimentações de estoque.
    """
    queryset = MovimentacaoEstoque.objects.all()
    serializer_class = MovimentacaoEstoqueSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
