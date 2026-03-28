from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

ILAN_KATEGORI = [
    # Satılık / Kiralık
    ('arac_satilik', 'Araç Satılık'),
    ('ev_kiralik', 'Ev / Daire Kiralık'),
    ('esya_satilik', 'Eşya / Mobilya Satılık'),
    ('diger_satilik', 'Diğer Satılık'),
    # Aranıyor
    ('arac_araniyor', 'Araç Aranıyor'),
    ('ev_araniyor', 'Ev / Oda Aranıyor'),
    ('is_araniyor', 'İş Arıyorum'),
    ('eleman_araniyor', 'Eleman Aranıyor'),
    ('esya_araniyor', 'Eşya / Mobilya Aranıyor'),
    ('diger_araniyor', 'Diğer Aranıyor'),
]

SATILIK_KATEGORILER = {'arac_satilik', 'ev_kiralik', 'esya_satilik', 'diger_satilik'}
ARANIYOR_KATEGORILER = {'arac_araniyor', 'ev_araniyor', 'is_araniyor', 'eleman_araniyor', 'esya_araniyor', 'diger_araniyor'}


class Ilan(models.Model):
    eyalet      = models.ForeignKey('stadt.Eyalet', null=True, blank=True, on_delete=SET_NULL, related_name='ilanlar', verbose_name='Eyalet')
    stadt       = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope       = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='stadt', verbose_name='Kapsam')
    sahip       = models.ForeignKey(User, on_delete=models.CASCADE)
    baslik      = models.CharField(max_length=200)
    icerik      = models.TextField()
    kategori    = models.CharField(max_length=20, choices=ILAN_KATEGORI)
    fiyat       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resim       = models.ImageField(upload_to='ilan/', blank=True, null=True, verbose_name='Resim')
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


class IlanYorum(models.Model):
    ilan        = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='yorumlar')
    yazar       = models.ForeignKey(User, on_delete=models.CASCADE)
    icerik      = models.TextField(max_length=1000)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['olusturulma']
        verbose_name = 'İlan Yorumu'
        verbose_name_plural = 'İlan Yorumları'

    def __str__(self):
        return f'{self.yazar.username} → {self.ilan.baslik[:40]}'
