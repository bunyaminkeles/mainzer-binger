from django.apps import AppConfig


class DuyurularConfig(AppConfig):
    name = 'duyurular'
    verbose_name = 'Duyurular'

    def ready(self):
        import duyurular.signals
