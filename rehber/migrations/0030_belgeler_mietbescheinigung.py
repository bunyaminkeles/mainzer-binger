from django.db import migrations


def guncelle(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    # Wohnungsgebende PDF'i Resmi Belgelerden kaldır
    Belge.objects.filter(
        harici_link__icontains='Wohnungsgebende-Bescheinigung-Formular'
    ).delete()

    # Mietbescheinigung'u Kaynak (Konut menüsü) den kaldır
    Kaynak.objects.filter(
        url__icontains='Mietbescheinigung'
    ).delete()

    # Mietbescheinigung'u Resmi Belgeler'e ekle
    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    Belge.objects.get_or_create(
        baslik='Mietbescheinigung — Kira Belgesi (Jobcenter Mainz)',
        stadt=mainz,
        defaults={
            'kategori':    'konut',
            'harici_link': 'https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',
            'ozet':        'Jobcenter Mainz kira belgesi formu — ev sahibine imzalatılır.',
            'yayinda':     True,
        }
    )


def geri_al(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    # Mietbescheinigung'u Belgelerden kaldır
    Belge.objects.filter(
        harici_link__icontains='Mietbescheinigung'
    ).delete()

    # Wohnungsgebende'yi Belgeler'e geri ekle
    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    Belge.objects.get_or_create(
        baslik='Wohnungsgeberbestätigung — Ev Sahibi Onay Belgesi (Mainz)',
        stadt=mainz,
        defaults={
            'kategori':    'konut',
            'harici_link': 'https://www.mainz.de/vv/medien/internet/Wohnungsgebende-Bescheinigung-Formular.pdf',
            'ozet':        'Mainz Bürgerbüro için ev sahibinden alınacak ikamet onay formu.',
            'yayinda':     True,
        }
    )

    # Mietbescheinigung'u Kaynak'a geri ekle
    Kaynak.objects.get_or_create(
        baslik='Mietbescheinigung — Kira Belgesi (PDF)',
        defaults={
            'tip':      'link',
            'url':      'https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',
            'kategori': 'konut',
            'icon':     'bi-file-earmark-pdf',
            'sira':     1,
            'yayinda':  True,
            'ozet':     'Jobcenter Mainz kira belgesi formu — ev sahibine imzalatılır.',
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0029_seed_belgeler_pdf'),
        ('stadt',  '0018_seed_koeln_stadt'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
