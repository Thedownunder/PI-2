from django.db import models
from clientes.models import Cliente
from phonenumber_field.modelfields import PhoneNumberField
from cpf_field.models import CPFField
from simple_history.models import HistoricalRecords
# Create your models here.

class Dependente(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = CPFField('cpf', null=False)
    nome = models.CharField(max_length=255)
    parentesco = models.CharField(max_length=100)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='dependentes' # Esta linha de código permite acessar os dependentes a partir do cliente.
    )
    telefone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    historico = HistoricalRecords()

    def __str__(self):
        return f"{self.nome} ({self.parentesco})"
    