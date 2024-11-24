from django.apps import AppConfig

class FuncionariosConfig(AppConfig):
    name = 'funcionarios'

    def ready(self):
        import funcionarios.signals
