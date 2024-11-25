from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Pet
from .serializers import PetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou editar pets.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    @action(detail=False, methods=['get'], url_path='do-cliente/(?P<cliente_cpf>[^/.]+)')
    def listar_pets_do_cliente(self, request, cliente_cpf=None):
        pets = Pet.objects.filter(cliente__cpf=cliente_cpf)
        serializer = self.get_serializer(pets, many=True)
        return Response(serializer.data)
