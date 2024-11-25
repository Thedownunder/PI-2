from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
class Produto(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField() # Colocamos somente como números positivos para não acontecer o erro da pessoa cadastrar errado.
    historico = HistoricalRecords()

    def __str__(self):
        return f"{self.nome} ({self.marca})"