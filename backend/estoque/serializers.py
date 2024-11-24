from rest_framework import serializers
from .models import MovimentacaoEstoque

class MovimentacaoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoEstoque
        fields = '__all__'  # Inclui todos os campos do modelo MovimentacaoEstoque
