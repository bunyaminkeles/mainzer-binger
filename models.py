from django.db import models
from django.conf import settings
from django.utils import timezone
from stadt.models import Stadt

class GlobalSetting(models.Model):
    is_business_module_active = models.BooleanField(default=False, help_text="Lokal Uzmanlar modülünü tüm site için açar veya kapar.")

    class Meta:
        verbose_name = "Modül Ayarı"
        verbose_name_plural = "Modül Ayarları"

    def __str__(self):
        return "Global Modül Ayarları"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BusinessCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap Icons sınıfı, ör: 'bi-shop'")

    class Meta:
        verbose_name = "İşletme Kategorisi"
        verbose_name_plural = "İşletme Kategorileri"

    def __str__(self):
        return self.name

class LocalBusiness(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_businesses',
        verbose_name="İşletme Sahibi"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    city = models.ForeignKey(Stadt, on_delete=models.PROTECT, verbose_name="Şehir")
    category = models.ForeignKey(BusinessCategory, on_delete=models.PROTECT, verbose_name="Kategori")
    slogan = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='businesses/logos/', blank=True, null=True)
    logo_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='businesses/covers/', blank=True, null=True)
    cover_image_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    instagram_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Yayında")
    is_verified = models.BooleanField(default=False, verbose_name="Doğrulanmış")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lokal Uzman"
        verbose_name_plural = "Lokal Uzmanlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def is_currently_active(self):
        if not self.is_published:
            return False
        if self.end_date and self.end_date < timezone.now().date():
            return False
        return True

class BusinessAnalytics(models.Model):
    business = models.ForeignKey(LocalBusiness, on_delete=models.CASCADE, related_name='analytics')
    date = models.DateField()
    views = models.PositiveIntegerField(default=0)
    whatsapp_clicks = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('business', 'date')
        verbose_name = "İşletme Analitiği"
        verbose_name_plural = "İşletme Analitikleri"
        ordering = ['-date']

    def __str__(self):
        return f"{self.business.name} - {self.date}"