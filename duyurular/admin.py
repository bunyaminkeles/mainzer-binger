from django.contrib import admin
from .models import Duyuru

@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'yayinda', 'olusturulma']
    list_filter  = ['kategori', 'yayinda']
    search_fields = ['baslik']
