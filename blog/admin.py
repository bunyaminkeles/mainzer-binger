from django.contrib import admin
from .models import BlogYazisi

@admin.register(BlogYazisi)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'yazar', 'eyalet', 'stadt', 'scope', 'yayinda', 'olusturulma']
    list_filter  = ['yayinda', 'eyalet', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
