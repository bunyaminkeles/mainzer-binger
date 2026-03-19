from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    kullanici     = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    biyografi     = models.TextField(blank=True)
    sehir         = models.CharField(max_length=100, blank=True, default='Mainz')
    gelis_tarihi  = models.DateField(null=True, blank=True)
    olusturulma   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profiller'

    def __str__(self):
        return f"{self.kullanici.username} profili"
