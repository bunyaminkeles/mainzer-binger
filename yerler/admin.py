from django.contrib import admin
from .models import Yer, YerFoto, ReklamPaketi


# ── Toplu işlem aksiyonları ──────────────────────────────────────────────────

@admin.action(description='Seçilenleri aktif yap')
def aktif_yap(modeladmin, request, queryset):
    queryset.update(aktif=True)

@admin.action(description='Seçilenleri pasif yap')
def pasif_yap(modeladmin, request, queryset):
    queryset.update(aktif=False)


# ── Yer ─────────────────────────────────────────────────────────────────────

class YerFotoInline(admin.TabularInline):
    model    = YerFoto
    extra    = 3
    fields   = ['foto', 'url', 'sira']
    ordering = ['sira']


@admin.register(Yer)
class YerAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'kategori', 'stadt', 'paket', 'paket_bitis', 'aktif_flag']
    list_filter   = ['paket', 'aktif', 'kategori', 'stadt', 'scope']
    list_editable = ['paket']
    search_fields = ['ad', 'adres']
    actions       = [aktif_yap, pasif_yap]
    inlines       = [YerFotoInline]
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'kategori', 'stadt', 'scope', 'aktif', 'adres', 'kapak_foto', 'kapak_resmi')
        }),
        ('İletişim', {
            'fields': ('telefon', 'website', 'maps_url', 'instagram_url', 'whatsapp', 'calisma_saati')
        }),
        ('Paket', {
            'fields': ('paket', 'paket_bitis'),
            'description': 'Ödeme yapıldığında paketi güncelleyin. Süre bittiğinde "Ücretsiz" olarak geri alın.',
        }),
        ('İçerik', {
            'fields': ('aciklama', 'icerik', 'wikipedia_url'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif


# ── ReklamPaketi ─────────────────────────────────────────────────────────────

@admin.register(ReklamPaketi)
class ReklamPaketiAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'fiyat', 'sure_etiketi', 'vurgulu', 'aktif_flag', 'sira']
    list_editable = ['vurgulu', 'sira']
    list_filter   = ['aktif', 'vurgulu']
    actions       = [aktif_yap, pasif_yap]
    fields        = ['ad', 'fiyat', 'sure_etiketi', 'renk', 'vurgulu', 'aktif', 'sira', 'ozellikler', 'iletisim_notu']

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif
