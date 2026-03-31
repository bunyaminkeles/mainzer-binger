from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class IlanConfig(AppConfig):
    name = 'ilan'

    def ready(self):
        logger.warning("🚀 [APP READY] İlan uygulaması başlatıldı ve sinyaller yükleniyor.")
        import ilan.signals
