from django.contrib import admin
from django.urls import path
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils.html import format_html

from .models import Eyalet, Stadt
from yerler.models import Yer, YerKategori
from rehber.models import Kaynak


@admin.register(Eyalet)
class EyaletAdmin(admin.ModelAdmin):
    list_display = ('ad', 'kod', 'slug', 'baskent', 'aktif', 'sehir_sayisi')
    list_editable = ('aktif',)
    prepopulated_fields = {'slug': ('ad',)}
    search_fields = ('ad', 'kod', 'baskent')
    actions = ['aktif_yap', 'pasif_yap']

    @admin.display(description='Şehir Sayısı')
    def sehir_sayisi(self, obj):
        return obj.sehirler.count()

    @admin.action(description='Seçili eyaletleri aktif et')
    def aktif_yap(self, request, queryset):
        queryset.update(aktif=True)

    @admin.action(description='Seçili eyaletleri pasif et')
    def pasif_yap(self, request, queryset):
        queryset.update(aktif=False)


@admin.register(Stadt)
class StadtAdmin(admin.ModelAdmin):
    list_display = ('name', 'eyalet', 'slug', 'typ', 'population', 'aktiv', 'onemli_yerler_btn')
    list_filter = ('eyalet', 'typ', 'aktiv')
    list_editable = ('aktiv',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    autocomplete_fields = ('eyalet',)
    actions = ['aktif_yap', 'pasif_yap']

    @admin.display(description='Önemli Yerler')
    def onemli_yerler_btn(self, obj):
        url = f'/admin/stadt/stadt/{obj.pk}/onemli-yerler/'
        return format_html(
            '<a href="{}" style="'
            'background:#2563eb;color:#fff;padding:3px 10px;border-radius:5px;'
            'font-size:.75rem;text-decoration:none;white-space:nowrap;">'
            '⚙ Yönet</a>',
            url
        )

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/onemli-yerler/',
                self.admin_site.admin_view(self.onemli_yerler_view),
                name='stadt_onemli_yerler',
            ),
        ]
        return custom + urls

    def onemli_yerler_view(self, request, pk):
        stadt = get_object_or_404(Stadt, pk=pk)

        if request.method == 'POST':
            action = request.POST.get('action')
            tab = request.POST.get('tab', '')

            yer_id = request.POST.get('yer_id')
            if yer_id:
                yer = get_object_or_404(Yer, pk=yer_id, stadt=stadt)
                if action == 'toggle_yer':
                    yer.aktif = not yer.aktif
                    yer.save()
                    durum = 'aktif' if yer.aktif else 'pasif'
                    messages.success(request, f'"{yer.ad}" {durum} yapıldı.')
                elif action == 'delete_yer':
                    ad = yer.ad
                    yer.delete()
                    messages.success(request, f'"{ad}" silindi.')

            kaynak_id = request.POST.get('kaynak_id')
            if kaynak_id:
                kaynak = get_object_or_404(Kaynak, pk=kaynak_id, stadt=stadt)
                if action == 'toggle_kaynak':
                    kaynak.yayinda = not kaynak.yayinda
                    kaynak.save()
                    durum = 'yayında' if kaynak.yayinda else 'pasif'
                    messages.success(request, f'"{kaynak.baslik}" {durum} yapıldı.')
                elif action == 'delete_kaynak':
                    baslik = kaynak.baslik
                    kaynak.delete()
                    messages.success(request, f'"{baslik}" silindi.')

            return redirect(f'{request.path}?tab={tab}')

        kategoriler = list(YerKategori.objects.filter(tur='yer').order_by('sira', 'ad'))
        yer_data = []
        for k in kategoriler:
            yerler = list(
                Yer.objects.filter(stadt=stadt, tur='yer', kategori=k.slug).order_by('ad')
            )
            yer_data.append({'kategori': k, 'yerler': yerler})

        kaynaklar = list(
            Kaynak.objects.filter(stadt=stadt, scope='stadt').order_by('sira', 'baslik')
        )

        aktif_tab = request.GET.get('tab', yer_data[0]['kategori'].slug if yer_data else 'baglanti')

        context = {
            **self.admin_site.each_context(request),
            'title': f'{stadt.name} — Önemli Yerler Yönetimi',
            'stadt': stadt,
            'yer_data': yer_data,
            'kaynaklar': kaynaklar,
            'aktif_tab': aktif_tab,
            'opts': Stadt._meta,
        }
        return render(request, 'admin/stadt/onemli_yerler.html', context)

    @admin.action(description='Seçili şehirleri aktif et')
    def aktif_yap(self, request, queryset):
        queryset.update(aktiv=True)

    @admin.action(description='Seçili şehirleri pasif et')
    def pasif_yap(self, request, queryset):
        queryset.update(aktiv=False)
