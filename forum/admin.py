from django.contrib import admin
from .models import ForumKategori, Konu, Yorum

admin.site.register(ForumKategori)

@admin.register(Konu)
class KonuAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'eyalet', 'stadt', 'scope', 'yazar', 'sabitlendi', 'kapali', 'olusturulma']
    list_filter  = ['kategori', 'sabitlendi', 'kapali', 'eyalet', 'stadt', 'scope']

@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ['konu', 'yazar', 'olusturulma']
