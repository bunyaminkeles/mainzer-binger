from django.db import models
from django.contrib.auth.models import User

ILAN_KATEGORI = [
    ('arac_satilik', 'Araç Satılık'),
    ('arac_araniyor', 'Araç Aranıyor'),
    ('ev_kiralik', 'Ev / Daire Kiralık'),
    ('ev_araniyor', 'Ev / Oda Aranıyor'),
    ('diger', 'Diğer'),
]

class Ilan(models.Model):
    sahip       = models.ForeignKey(User, on_delete=models.CASCADE)
    baslik      = models.CharField(max_length=200)
    icerik      = models.TextField()
    kategori    = models.CharField(max_length=20, choices=ILAN_KATEGORI)
    fiyat       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    iletisim    = models.EmailField()
    aktif       = models.BooleanField(default=True)
    onaylandi   = models.BooleanField(default=False)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'İlan'
        verbose_name_plural = 'İlanlar'

    def __str__(self):
        return self.baslik
