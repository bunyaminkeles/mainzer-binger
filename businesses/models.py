from django.db import models
from django.utils import timezone
from django.conf import settings


class GlobalSetting(models.Model):
    """Singleton — tek satır. İşletme modülünü açıp kapar."""
    is_business_module_active = models.BooleanField(
        default=False,
        verbose_name='İşletme Modülü Aktif',
        help_text='Navbar menüsü ve tüm işletme sayfaları bu şalterle açılır/kapanır.',
    )

    class Meta:
        verbose_name = 'Global Ayar'
        verbose_name_plural = 'Global Ayarlar'

    def __str__(self):
        durum = 'AKTİF' if self.is_business_module_active else 'KAPALI'
        return f'İşletme Modülü — {durum}'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SubscriptionPlan(models.Model):
    """Abonelik paketleri — Standart, Gold, VIP vb."""
    name = models.CharField(max_length=100, verbose_name='Paket Adı')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Fiyat (€)')
    duration_days = models.PositiveIntegerField(verbose_name='Süre (Gün)', help_text='Örn: 30, 90, 365')
    is_active = models.BooleanField(default=True, verbose_name='Aktif')

    class Meta:
        ordering = ['price']
        verbose_name = 'Abonelik Paketi'
        verbose_name_plural = 'Abonelik Paketleri'

    def __str__(self):
        return f'{self.name} ({self.duration_days} gün — €{self.price})'


class BusinessCategory(models.Model):
    """İşletme kategorileri — Restoran, Berber, Avukat vb."""
    name = models.CharField(max_length=100, verbose_name='Kategori Adı')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
    icon = models.CharField(max_length=50, blank=True, verbose_name='İkon (Bootstrap Icon sınıfı)')

    class Meta:
        ordering = ['name']
        verbose_name = 'İşletme Kategorisi'
        verbose_name_plural = 'İşletme Kategorileri'

    def __str__(self):
        return self.name


class LocalBusiness(models.Model):
    """Ana işletme modeli — tüm rehber kartlarının kaynağı."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_businesses',
        verbose_name="İşletme Sahibi"
    )

    # — Kimlik —
    name = models.CharField(max_length=200, verbose_name='İşletme Adı')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
    city = models.ForeignKey(
        'stadt.Stadt',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='businesses',
        verbose_name='Şehir',
    )
    category = models.ForeignKey(
        BusinessCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='businesses',
        verbose_name='Kategori',
    )

    # — İçerik —
    slogan = models.CharField(max_length=150, blank=True, verbose_name='Slogan')
    description = models.TextField(blank=True, verbose_name='Açıklama')

    # — Medya —
    logo = models.ImageField(upload_to='businesses/logos/', blank=True, null=True, verbose_name='Logo (dosya)')
    logo_url = models.URLField(blank=True, verbose_name='Logo URL', help_text='Dosya yerine harici link kullanmak için')
    cover_image = models.ImageField(upload_to='businesses/covers/', blank=True, null=True, verbose_name='Kapak Görseli (dosya)')
    cover_image_url = models.URLField(blank=True, verbose_name='Kapak Görseli URL', help_text='Dosya yerine harici link kullanmak için')

    # — İletişim —
    whatsapp_number = models.CharField(max_length=30, blank=True, verbose_name='WhatsApp Numarası', help_text='+49 ile başlamalı')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram URL')
    website_url = models.URLField(blank=True, verbose_name='Web Sitesi')

    # — Yönetim & Paket —
    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='businesses',
        verbose_name='Abonelik Paketi',
    )
    start_date = models.DateField(null=True, blank=True, verbose_name='Başlangıç Tarihi')
    end_date = models.DateField(null=True, blank=True, verbose_name='Bitiş Tarihi')
    is_published = models.BooleanField(default=False, verbose_name='Yayında')
    is_verified = models.BooleanField(default=False, verbose_name='Onaylı İşletme')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Yerel İşletme'
        verbose_name_plural = 'Yerel İşletmeler'

    def __str__(self):
        return f'{self.name} ({self.city})'

    @property
    def is_currently_active(self) -> bool:
        """Hem yayında olmalı hem de abonelik süresi dolmamış olmalı."""
        if not self.is_published:
            return False
        if self.end_date is None:
            return False
        return self.end_date >= timezone.localdate()


class BusinessAnalytics(models.Model):
    """Günlük görüntülenme ve WhatsApp tıklama sayaçları."""
    business = models.ForeignKey(
        LocalBusiness,
        on_delete=models.CASCADE,
        related_name='analytics',
        verbose_name='İşletme',
    )
    date = models.DateField(verbose_name='Tarih')
    views = models.PositiveIntegerField(default=0, verbose_name='Görüntülenme')
    whatsapp_clicks = models.PositiveIntegerField(default=0, verbose_name='WhatsApp Tıklaması')

    class Meta:
        unique_together = ('business', 'date')
        ordering = ['-date']
        verbose_name = 'İşletme Analitik'
        verbose_name_plural = 'İşletme Analitikleri'

    def __str__(self):
        return f'{self.business.name} — {self.date}'
