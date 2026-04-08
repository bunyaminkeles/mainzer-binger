from django.apps import AppConfig


class IlanConfig(AppConfig):
    name = 'ilan'
    verbose_name = 'İlanlar'

    def ready(self):
        import ilan.signals
