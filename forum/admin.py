from django.contrib import admin
from .models import ForumKategori, Konu, Yorum


class YorumInline(admin.TabularInline):
    model = Yorum
    extra = 0
    fields = ['yazar', 'olusturulma']
    readonly_fields = ['yazar', 'olusturulma']


@admin.register(ForumKategori)
class ForumKategoriAdmin(admin.ModelAdmin):
    list_display = ['ad']


@admin.register(Konu)
class KonuAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'eyalet', 'stadt', 'scope', 'yazar', 'sabitlendi', 'kapali', 'olusturulma']
    list_filter  = ['kategori', 'sabitlendi', 'kapali', 'eyalet', 'stadt', 'scope']
    inlines      = [YorumInline]
