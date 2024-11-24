from rest_framework import serializers
from .models import Cliente
from dependentes.serializers import DependenteSerializer  # Importa o serializer de dependentes

class ClienteSerializer(serializers.ModelSerializer):
    dependentes = DependenteSerializer(many=True, read_only=True)  # Inclui os dependentes do cliente
    data_nascimento = serializers.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Cliente
        fields = '__all__'  # Inclui todos os campos do modelo Cliente
