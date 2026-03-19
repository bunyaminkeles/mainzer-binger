from django.contrib import admin
from .models import RehberSayfasi

@admin.register(RehberSayfasi)
class RehberAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'sira', 'yayinda']
    list_filter  = ['kategori', 'yayinda']
    prepopulated_fields = {'slug': ('baslik',)}
