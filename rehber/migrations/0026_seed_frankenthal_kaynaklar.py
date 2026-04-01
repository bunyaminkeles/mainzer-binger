from django.db import migrations

KAYNAKLAR = [
    # Resmi
    dict(
        kategori='resmi',
        baslik='Ausländerbehörde Frankenthal',
        url='https://www.frankenthal.de/stadt-frankenthal/de/rathaus/buergerservice/dienstleistungen/auslaenderwesen/',
        ozet='Frankenthal Yabancılar Dairesi: Oturma izni, vize uzatma ve vatandaşlık işlemleri.',
        icon='bi-building-fill',
        sira=1,
    ),
    dict(
        kategori='resmi',
        baslik='Bürgerservice Frankenthal – Online Termin',
        url='https://www.frankenthal.de/stadt-frankenthal/de/rathaus/buergerservice/online-terminvergabe/',
        ozet='Anmeldung (ikamet kaydı), pasaport ve diğer vatandaşlık hizmetleri için online randevu sistemi.',
        icon='bi-person-vcard-fill',
        sira=2,
    ),
    # İş
    dict(
        kategori='is',
        baslik='Jobcenter Vorderpfalz-Ludwigshafen (Frankenthal)',
        url='https://www.jobcenter-vorderpfalz.de/',
        ozet='Bürgergeld başvurusu, iş arama desteği ve Frankenthal bölgesine bakan Jobcenter merkezi.',
        icon='bi-briefcase-fill',
        sira=1,
    ),
    # Konut
    dict(
        kategori='konut',
        baslik='Frankenthal KdU – Kira Üst Limitleri',
        url='https://harald-thome.de/files/pdf/KdU/KdU%20Frankenthal%20-%2001.01.2023.pdf',
        ozet='Jobcenter tarafından Frankenthal için kabul edilen güncel uygun kira (Mietobergrenzen) ve ısınma bedeli limitleri.',
        icon='bi-house-fill',
        sira=1,
    ),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        sehir = Stadt.objects.get(slug='frankenthal')
    except Stadt.DoesNotExist:
        return

    # Ana sayfa (hero) linklerini güncelle
    sehir.auslaenderbehorde_url = 'https://www.frankenthal.de/stadt-frankenthal/de/rathaus/buergerservice/dienstleistungen/auslaenderwesen/'
    sehir.termin_url = 'https://www.frankenthal.de/stadt-frankenthal/de/rathaus/buergerservice/online-terminvergabe/'
    sehir.save()

    for d in KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=sehir,
            defaults={**d, 'eyalet': sehir.eyalet, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    basliklar = [d['baslik'] for d in KAYNAKLAR]
    Kaynak.objects.filter(baslik__in=basliklar, stadt__slug='frankenthal').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0025_seed_berlin_kaynaklar'),
        # ('yerler', '0028_seed_frankenthal_yerler') # Sıralama açısından referans
    ]
    
    operations = [
        migrations.RunPython(seed, unseed)
    ]