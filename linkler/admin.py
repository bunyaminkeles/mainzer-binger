from django.contrib import admin
from .models import OnemliLink

@admin.register(OnemliLink)
class OnemliLinkAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'kategori', 'eyalet', 'stadt', 'scope', 'sira', 'aktif']
    list_filter   = ['kategori', 'aktif', 'eyalet', 'stadt', 'scope']
    search_fields = ['ad']
    list_editable = ['sira', 'aktif']
