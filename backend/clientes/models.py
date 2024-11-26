from django.db import models
from phonenumber_field.modelfields import PhoneNumberField # Campo para números de telefone.
from cpf_field.models import CPFField # Biblioteca para validar CPF
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
import re
# Create your models here.

def validate_cep(value):
    pattern = r'^\d{5}-\d{3}$'
    if not re.match(pattern, value):
        raise ValidationError('CEP inválido. Use o formato 00000-000.')


class Cliente(models.Model):
    cpf = CPFField('CPF',
                   primary_key=True,
                   unique=True
                   )
    nome_completo = models.CharField(max_length=255)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    telefone = PhoneNumberField() # Campo com validação de número de telefone.
    cep = models.CharField(
        max_length=9,
        validators=[validate_cep],
        help_text='Formato: 00000-000'
    )  # CEP no formato 00000-000
    
    numero = models.PositiveIntegerField()
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    UF_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]
    uf = models.CharField(max_length=2, choices=UF_CHOICES)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True) # Preenche automaticamente a data em que o cliente foi cadastrado no sistema.
    vale_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    crediario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    historico = HistoricalRecords()  # Adiciona histórico para auditoria

    def __str__(self):
        return self.nome_completo # Retorna o nome do cliente, representando ele como string.
    


