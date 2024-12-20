# Generated by Django 5.1.3 on 2024-11-24 06:08

import cpf_field.models
import django.db.models.deletion
import funcionarios.models
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('chave', models.CharField(editable=False, max_length=8, unique=True)),
                ('cpf', cpf_field.models.CPFField(max_length=14, primary_key=True, serialize=False, unique=True, verbose_name='CPF')),
                ('nome_completo', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('cep', models.CharField(help_text='Formato: 00000-000', max_length=9, validators=[funcionarios.models.validate_cep])),
                ('numero', models.PositiveIntegerField()),
                ('endereco', models.CharField(max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('data_nascimento', models.DateField()),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('cargo', models.CharField(max_length=100)),
                ('must_change_password', models.BooleanField(default=False)),
                ('password_last_changed', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
