from rest_framework import serializers
from .models import Agendamento
from pets.serializers import PetSerializer  # Para exibir detalhes do pet

class AgendamentoSerializer(serializers.ModelSerializer):
    telefone = serializers.CharField(source='cliente.telefone', read_only=True) # Inclui o telefone do dono do pet.
    pet = PetSerializer(read_only=True)  # Inclui detalhes do pet

    class Meta:
        model = Agendamento
        fields = '__all__'  # Inclui todos os campos do modelo Agendamento
