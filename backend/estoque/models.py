from django.db import models
from produtos.models import Produto
from simple_history.models import HistoricalRecords
# Create your models here.
class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)
    historico = HistoricalRecords()

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome}"
    
    def save(self, *args, **kwargs):
        # Ao salvar uma movimentação, atualizamos o estoque do produto
        if self.tipo == 'E':
            self.produto.estoque += self.quantidade # Entrada de produto: Soma-se ao estoque
        elif self.tipo == 'S':
            self.produto.estoque -= self.quantidade # Saída de produto: subtrai do estoque
        self.produto.save() # Salva a atualização no produto
        super().save(*args, **kwargs) # Chama o método save original