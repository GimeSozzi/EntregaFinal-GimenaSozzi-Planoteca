from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AppUsuariosConfig(AppConfig):
    name = 'app_usuarios'

    def ready(self):
        from . import signals  # Importa los signals de tu app

