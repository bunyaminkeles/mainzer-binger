from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import logging
from .models import Ilan

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Ilan)
def ilan_onay_bildirimi(sender, instance, created, **kwargs):
    logger.warning(f"🔔 [SİNYAL TETİKLENDİ] İlan: {instance.baslik} | Yeni mi?: {created}")

    # İlan yeni oluşturulduysa ve onay bekliyorsa
    if created and not getattr(instance, 'onaylandi', True):
        logger.warning("📩 [SİNYAL] Şartlar sağlandı, e-posta gönderimi başlatılıyor...")
        subject = f'[Onay Bekliyor] Yeni İlan: {instance.baslik}'
        message = (
            f"Sistemde onayınızı bekleyen yeni bir ilan eklendi.\n\n"
            f"Başlık: {instance.baslik}\n"
            f"Kullanıcı: {instance.sahip.username if instance.sahip else 'Bilinmiyor'}\n\n"
            f"İncelemek ve onaylamak için admin paneline gidin:\n"
            f"https://almanyalirehber.com/admin/ilan/ilan/{instance.id}/change/"
        )
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'info@almanyalirehber.com'),
                recipient_list=['info@analizus.com'],
                fail_silently=False,  # Hatayı bilerek fırlatmasını istiyoruz ki logda görelim
            )
            logger.warning("✅ [SİNYAL] E-posta başarıyla gönderildi!")
        except Exception as e:
            logger.error(f"❌ [SİNYAL HATASI] E-posta gönderilemedi: {e}")