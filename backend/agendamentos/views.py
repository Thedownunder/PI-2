from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Agendamento
from .serializers import AgendamentoSerializer
# Create your views here.

class AgendamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou agendar serviços.
    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_create(self, serializer):
        # Validação para evitar conflitos de horário
        data = serializer.validated_data['data']
        horario = serializer.validated_data['horario']
        funcionario = serializer.validated_data['funcionario']

        if Agendamento.objects.filter(data=data, horario=horario, funcionario=funcionario).exists():
            raise serializers.ValidationError("Este horário já está ocupado para o funcionário selecionado.")
        serializer.save()

