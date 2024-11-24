from rest_framework import serializers
from .models import Venda, ItemVenda
from produtos.models import Produto

class ItemVendaSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = ItemVenda
        fields = ['id', 'produto', 'quantidade', 'preco_unitario', 'total_item']
        read_only_fields = ['total_item']


class VendaSerializer(serializers.ModelSerializer):
    desconto = serializers.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        model = Venda
        fields = [
            'id', 'cliente', 'funcionario', 'data_venda',
            'valor_total', 'metodo_pagamento', 'status',
            'desconto', 'itens'
        ]

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')  # Remove os dados dos itens
        venda = Venda.objects.create(**validated_data)  # Cria a venda
        for item_data in itens_data:
            ItemVenda.objects.create(venda=venda, **item_data)  # Cria cada item da venda
        venda.calcular_valor_total()  # Atualiza o valor total da venda
        return venda
