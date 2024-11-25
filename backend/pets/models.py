from django.db import models
from clientes.models import Cliente
# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cor_pelagem = models.CharField(max_length=50)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pets' # Permite acessar os pets a partir do cliente.
    )

    def __str__(self):
        return f"{self.nome} - {self.cliente} ({self.cliente.cpf})"