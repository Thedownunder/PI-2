from cpf_field.models import CPFField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import re
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import random
# Create your models here.

def validate_cep(value):
    pattern = r'^\d{5}-\d{3}$'
    if not re.match(pattern, value):
        raise ValidationError('CEP inválido. Use o formato 00000-000.')

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario')  # Relacionamento com User
    chave = models.CharField(max_length=8, unique=True, editable=False)
    cpf = CPFField('CPF',
                   primary_key=True,
                   unique=True)
    nome_completo = models.CharField(max_length=255)

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefone = PhoneNumberField(null=False, blank=False, unique=True)
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
    data_nascimento = models.DateField()
    data_inicio = models.DateField(auto_now_add=True)
    cargo = models.CharField(max_length=100)
    must_change_password = models.BooleanField(default=False)
    password_last_changed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf}) - Cargo: {self.cargo}"
    
    def save(self, *args, **kwargs):
        if not self.chave:
            self.chave = self.gerar_chave_unica()
        super().save(*args, **kwargs)

    def gerar_chave_unica(self):
        while True:
            numero = random.randint(1, 9999999)
            chave = f'F{numero:07d}'
            if not Funcionario.objects.filter(chave=chave).exists():
                return chave

    def password_expired(self):
        # Verifica se a senha expirou (6 meses)
        expiration_date = self.password_last_changed + timedelta(days=180)
        return timezone.now() > expiration_date
    
    def days_until_expiration(self):
        # Calcula o número de dias até a expiração da senha
        expiration_date = self.password_last_changed + timedelta(days=180)
        delta = expiration_date - timezone.now()
        return delta.days
