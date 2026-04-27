from django.apps import AppConfig
from django.urls import register_converter


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Converters'ı burada kaydetmek, uygulamanın yüklendiğinde bir kez çalışmasını sağlar.
        from config.converters import EyaletConverter
        register_converter(EyaletConverter, 'eyalet')