from django.contrib import admin
from .models import Kaynak

@admin.register(Kaynak)
class KaynakAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tip', 'kategori', 'eyalet', 'stadt', 'scope', 'sira', 'yayinda']
    list_filter  = ['tip', 'kategori', 'yayinda', 'eyalet', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
    list_editable = ['sira', 'yayinda']
