from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Funcionario

@receiver(post_save, sender=User)
def criar_perfil_funcionario(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        # Apenas cria o perfil se o usuário não for um superusuário
        Funcionario.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil_funcionario(sender, instance, **kwargs):
    if not instance.is_superuser:
        # Verifica se o perfil existe antes de tentar salvar
        try:
            instance.funcionario.save()
        except Funcionario.DoesNotExist:
            # O perfil não existe, então não faz nada
            pass
