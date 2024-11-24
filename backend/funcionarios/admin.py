from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_completo', 'chave', 'user')
    search_fields = ('nome_completo', 'chave', 'user__username')
