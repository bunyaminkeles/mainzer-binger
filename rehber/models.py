from django.db import models

REHBER_KATEGORI = [
    ('resmi', 'Resmi İşlemler'),
    ('gunluk', 'Günlük Yaşam'),
    ('egitim', 'Eğitim'),
    ('saglik', 'Sağlık'),
    ('ulasim', 'Ulaşım'),
    ('konut', 'Konut'),
    ('almanca', 'Almanca Çalışma'),
    ('gezi', 'Gezi & Kültür'),
]

class RehberSayfasi(models.Model):
    baslik      = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, max_length=220)
    kategori    = models.CharField(max_length=20, choices=REHBER_KATEGORI)
    icerik      = models.TextField()
    ozet        = models.CharField(max_length=300, blank=True)
    icon        = models.CharField(max_length=50, default='bi-info-circle')
    sira        = models.PositiveIntegerField(default=0)
    yayinda     = models.BooleanField(default=True)
    guncelleme  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['kategori', 'sira']
        verbose_name = 'Rehber Sayfası'
        verbose_name_plural = 'Rehber Sayfaları'

    def __str__(self):
        return self.baslik
