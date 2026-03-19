from django.contrib import admin
from .models import BlogYazisi

@admin.register(BlogYazisi)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'yazar', 'yayinda', 'olusturulma']
    list_filter  = ['yayinda']
    prepopulated_fields = {'slug': ('baslik',)}
