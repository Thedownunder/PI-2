from django.db import models
from pets.models import Pet
from clientes.models import Cliente
from funcionarios.models import Funcionario
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
        ('Concluído', 'Concluído'),
    ]
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    servico = models.CharField(max_length=100)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        null=True
    )
    telefone = PhoneNumberField()
    observacao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.servico} para {self.pet.nome} em {self.data} às {self.horario}"
    
    class Meta:
        unique_together = ('data', 'horario', 'funcionario') # Garante que um funcionário não tenha dois agendamentos no mesmo horário
        