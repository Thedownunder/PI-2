from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Dependente
from .serializers import DependenteSerializer
# Create your views here.

class DependenteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou editar dependentes.
    """
    queryset = Dependente.objects.all()
    serializer_class = DependenteSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
