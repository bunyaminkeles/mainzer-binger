"""
Data migration: Mainz-Bingen'e özel linkler eklenir, Mainz URL'li ortak linkler düzeltilir.

- Mainz'e özel URL içeren linkler scope='stadt' yapılır.
- Mainz-Bingen için Kreis Portalı ve Jobcenter eklenir.
- Ortak platformlar (Kleinanzeigen vb.) generic URL ile eyalet kalır.
"""
from django.db import migrations


def ekle_ve_duzenle(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    # --- Mainz'e özel URL'li linkleri scope='stadt' yap ---
    # Kleinanzeigen /s-mainz/, ImmobilienScout24 /mainz/, Immonet /mainz.html
    mainz_url_patterns = ['kleinanzeigen.de/s-mainz', 'immobilienscout24.de/Suche/de/rheinland-pfalz/mainz', 'immonet.de/immobiliensuche/mainz']
    for pattern in mainz_url_patterns:
        OnemliLink.objects.filter(url__icontains=pattern, scope='eyalet').update(
            scope='stadt', stadt=mainz
        )

    # --- Mainz-Bingen için şehre özel linkler ---
    mb_linkler = [
        dict(
            ad='Kreis Mainz-Bingen Portalı',
            url='https://www.kreis-mainz-bingen.de/',
            kategori='resmi',
            aciklama='Landkreis Mainz-Bingen resmi sitesi — haberler, hizmetler, vatandaş işlemleri.',
            sira=2,
            stadt=mainz_bingen,
            scope='stadt',
            aktif=True,
        ),
        dict(
            ad='Jobcenter Mainz-Bingen',
            url='https://www.jobcenter-mainz-bingen.de/',
            kategori='is',
            aciklama='Mainz-Bingen Jobcenter — işsizlik yardımı, iş arama desteği ve sosyal yardım başvuruları.',
            sira=1,
            stadt=mainz_bingen,
            scope='stadt',
            aktif=True,
        ),
        dict(
            ad='Kleinanzeigen — Mainz-Bingen',
            url='https://www.kleinanzeigen.de/s-bingen-rhein/c0',
            kategori='ilan',
            aciklama='Kleinanzeigen üzerinde Mainz-Bingen bölgesi ilanları.',
            sira=1,
            stadt=mainz_bingen,
            scope='stadt',
            aktif=True,
        ),
        dict(
            ad='ImmobilienScout24 — Mainz-Bingen',
            url='https://www.immobilienscout24.de/Suche/de/rheinland-pfalz/mainz-bingen/wohnung-mieten',
            kategori='ilan',
            aciklama='Mainz-Bingen ilçesinde kiralık ev ilanları.',
            sira=2,
            stadt=mainz_bingen,
            scope='stadt',
            aktif=True,
        ),
    ]

    for link_data in mb_linkler:
        OnemliLink.objects.get_or_create(url=link_data['url'], defaults=link_data)

    # --- Mainz için de Kleinanzeigen ve ImmobilienScout24 varsa güncelle ---
    OnemliLink.objects.filter(
        url__icontains='kleinanzeigen.de/s-mainz', scope='stadt'
    ).update(ad='Kleinanzeigen — Mainz', stadt=mainz)

    OnemliLink.objects.filter(
        url__icontains='immobilienscout24.de/Suche/de/rheinland-pfalz/mainz', scope='stadt'
    ).update(ad='ImmobilienScout24 — Mainz', stadt=mainz)

    OnemliLink.objects.filter(
        url__icontains='immonet.de/immobiliensuche/mainz', scope='stadt'
    ).update(ad='Immonet — Mainz', stadt=mainz)


def geri_al(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    # Mainz-özel yapılanları geri eyalet'e al
    mainz_url_patterns = ['kleinanzeigen.de/s-mainz', 'immobilienscout24.de/Suche/de/rheinland-pfalz/mainz', 'immonet.de/immobiliensuche/mainz']
    for pattern in mainz_url_patterns:
        OnemliLink.objects.filter(url__icontains=pattern, scope='stadt', stadt=mainz).update(
            scope='eyalet', stadt=None
        )

    # Mainz-Bingen'e özelleri sil
    OnemliLink.objects.filter(stadt=mainz_bingen, scope='stadt').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('linkler', '0002_onemlilink_scope_onemlilink_stadt'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(ekle_ve_duzenle, geri_al),
    ]
