from django.contrib import admin
from .models import Etkinlik

@admin.register(Etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih', 'tur']
    list_filter  = ['tur']
