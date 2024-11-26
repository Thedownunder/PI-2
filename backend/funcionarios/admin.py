from django.contrib import admin
from .models import Funcionario
from django.contrib.auth.models import User


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_completo', 'chave', 'user')
    search_fields = ('nome_completo', 'chave', 'user__username')

    # Campos que serão exibidos no formulário
    fields = ('nome_completo', 'cpf', 'user')

    def save_model(self, request, obj, form, change):
        # Se o objeto ainda não existir (novo funcionário)
        if not obj.pk:
            # Gerar a chave única
            obj.chave = obj.gerar_chave_unica()
            # Criar o usuário associado
            user = User.objects.create_user(
                username=obj.chave,
                password='SenhaInicial123!'  # Defina uma senha inicial ou gere uma aleatória
            )
            obj.user = user
        super().save_model(request, obj, form, change)

