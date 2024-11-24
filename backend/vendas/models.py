from django.db import models
from clientes.models import Cliente
from funcionarios.models import Funcionario
from produtos.models import Produto
from estoque.models import MovimentacaoEstoque
from simple_history.models import HistoricalRecords
# Create your models here.
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente,
                                on_delete=models.SET_NULL,
                                null=True)
    funcionario = models.ForeignKey(Funcionario,
                                    on_delete=models.SET_NULL,
                                    null=True)
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        help_text='Desconto em porcentagem (0-100)'
    )
    PAGAMENTO_CHOICES = [
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito'),
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
    ]
    metodo_pagamento = models.CharField(max_length=8, choices=PAGAMENTO_CHOICES)
    historico = HistoricalRecords()

    def __str__(self):
        return f"Venda {self.id} - {self.data_venda}"
    
    def calcular_valor_total(self):
        total = sum(item.total_item for item in self.itens.all())
        # Aplica o desconto
        total_com_desconto = total - (total * (self.desconto / 100))
        self.valor_total = total_com_desconto
        self.save()
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        related_name='itens',
        on_delete=models.CASCADE
    )
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_item = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    historico = HistoricalRecords()

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
    
    def save(self, *args, **kwargs):
        # Calcula o total do item
        self.total_item = self.preco_unitario * self.quantidade
        super().save(*args, **kwargs)
        # Atualiza o valor total da venda
        self.venda.calcular_valor_total()
        # Atualiza o estoque do produto
        movimentacao = MovimentacaoEstoque(
            produto=self.produto,
            tipo='S',
            quantidade=self.quantidade,
            observacao=f"ID da Venda: {self.venda.id}"
        )
        movimentacao.save()