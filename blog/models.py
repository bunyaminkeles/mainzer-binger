from django.db import models
from django.contrib.auth.models import User

class BlogYazisi(models.Model):
    baslik      = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, max_length=220)
    yazar       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    icerik      = models.TextField()
    ozet        = models.CharField(max_length=300, blank=True)
    yayinda     = models.BooleanField(default=False)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

    def __str__(self):
        return self.baslik
