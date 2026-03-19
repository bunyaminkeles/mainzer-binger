from django.db import models

KAYNAK_KATEGORI = [
    ('resmi', 'Resmi İşlemler & Kurumlar'),
    ('ilan', 'İlan Platformları'),
    ('is', 'İş & Kariyer'),
    ('konut', 'Konut'),
    ('egitim', 'Eğitim'),
    ('saglik', 'Sağlık'),
    ('ulasim', 'Ulaşım'),
    ('almanca', 'Almanca Öğrenimi'),
    ('gunluk', 'Günlük Yaşam'),
    ('gezi', 'Gezi & Kültür'),
    ('haber', 'Haber & Bilgi'),
    ('diger', 'Diğer'),
]

KAYNAK_TIPI = [
    ('sayfa', 'Dahili Sayfa'),
    ('link', 'Harici Link'),
]

class Kaynak(models.Model):
    baslik      = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=220, unique=True, blank=True, null=True, help_text='Sadece dahili sayfalar için kullanılır.')
    tip         = models.CharField(max_length=10, choices=KAYNAK_TIPI, default='sayfa')
    url         = models.URLField(blank=True, help_text='Sadece harici linkler için kullanılır.')
    kategori    = models.CharField(max_length=20, choices=KAYNAK_KATEGORI)
    icerik      = models.TextField(blank=True, help_text='Sadece dahili sayfalar için kullanılır.')
    ozet        = models.CharField(max_length=300, blank=True)
    icon        = models.CharField(max_length=50, default='bi-info-circle')
    sira        = models.PositiveIntegerField(default=0)
    yayinda     = models.BooleanField(default=True)
    guncelleme  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['kategori', 'sira']
        verbose_name = 'Kaynak'
        verbose_name_plural = 'Kaynaklar'

    def __str__(self):
        return self.baslik
