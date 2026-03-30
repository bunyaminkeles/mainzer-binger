from django.db import migrations


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Belge  = apps.get_model('rehber', 'Belge')
    Stadt  = apps.get_model('stadt', 'Stadt')

    # ── Hamburg KdU URL güncelle ──────────────────────────────────
    Kaynak.objects.filter(
        baslik='Hamburg KdU Tablosu (PDF)',
        stadt__slug='hamburg',
    ).update(
        url='https://www.hamburg.de/resource/blob/45120/879d7f4de0deba3bcbf2f224668d4898/fa-sgbxii-35-kdu-05-angemessenheitsgrenzen-bruttokaltmiete-data.pdf',
        baslik='Hamburg KdU — Angemessenheitsgrenzen Bruttokaltmiete (PDF)',
        ozet='Hamburg\'da § 22 SGB II ve § 35 SGB XII kapsamındaki güncel brüt soğuk kira tavan değerleri tablosu.',
    )

    # ── Worms KdU Kaynak ekle ─────────────────────────────────────
    try:
        worms = Stadt.objects.get(slug='worms')
    except Stadt.DoesNotExist:
        pass
    else:
        Kaynak.objects.get_or_create(
            baslik='Worms KdU — Kosten der Unterkunft Bilgisi',
            stadt=worms,
            defaults={
                'tip':      'link',
                'url':      'https://jobcenter-worms.de/geldleistungen/kosten-fuer-unterkunft-und-heizung/',
                'kategori': 'konut',
                'icon':     'bi-house-fill',
                'sira':     5,
                'yayinda':  True,
                'ozet':     '§ 22 SGB II kapsamında Worms\'da Jobcenter tarafından karşılanan kira tavan değerleri ve konut yardımı bilgisi.',
                'eyalet':   worms.eyalet,
                'scope':    'stadt',
            }
        )

    # ── Trier KdU Kaynak ekle ─────────────────────────────────────
    try:
        trier = Stadt.objects.get(slug='trier')
    except Stadt.DoesNotExist:
        pass
    else:
        Kaynak.objects.get_or_create(
            baslik='Trier KdU — Hinweisblatt Kosten der Unterkunft 2024 (PDF)',
            stadt=trier,
            defaults={
                'tip':      'link',
                'url':      'https://www.jobcenter-trier-stadt.de/fileadmin/user_upload/bilder/Antr%C3%A4ge_und_Formulare/Hinweisblatt_Kosten_der_Unterkunft_2024.pdf',
                'kategori': 'konut',
                'icon':     'bi-file-earmark-pdf',
                'sira':     5,
                'yayinda':  True,
                'ozet':     '§ 22 SGB II kapsamında Trier\'da anlaşılan kira sınır değerleri — Jobcenter Trier Stadt (2024).',
                'eyalet':   trier.eyalet,
                'scope':    'stadt',
            }
        )

    # ── Mannheim Miet-Angebotsbescheinigung Belge ekle ────────────
    try:
        mannheim = Stadt.objects.get(slug='mannheim')
    except Stadt.DoesNotExist:
        pass
    else:
        Belge.objects.get_or_create(
            baslik='Miet-Angebotsbescheinigung — Kira Teklif Belgesi (Jobcenter 2025)',
            stadt=mannheim,
            defaults={
                'kategori':   'konut',
                'harici_link': 'https://www.jobcenter-vorderpfalz-ludwigshafen.de/images/jclh/downloadcenter/Miet-Angebotsbescheinigung-Jobcenter-Vorderpfalz-Ludwigshafen-2025.pdf',
                'ozet':       'Yeni kiralık daire başvurusunda ev sahibine imzalatılacak kira teklif belgesi formu (2025).',
                'yayinda':    True,
            }
        )


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Belge  = apps.get_model('rehber', 'Belge')

    # Hamburg'u eski haline döndür
    Kaynak.objects.filter(
        baslik='Hamburg KdU — Angemessenheitsgrenzen Bruttokaltmiete (PDF)',
        stadt__slug='hamburg',
    ).update(
        url='https://www.hamburg.de/resource/blob/46622/65d07f3444e21ac56fdac0c3155897d4/fa-sgbii-22-kdu-00-pdf-data.pdf',
        baslik='Hamburg KdU Tablosu (PDF)',
        ozet='Hamburg Sosyal Yardım Dairesi\'nin § 22 SGB II kapsamındaki güncel kira tavan değerleri (Kosten der Unterkunft) tablosu.',
    )

    Kaynak.objects.filter(baslik='Worms KdU — Kosten der Unterkunft Bilgisi', stadt__slug='worms').delete()
    Kaynak.objects.filter(baslik='Trier KdU — Hinweisblatt Kosten der Unterkunft 2024 (PDF)', stadt__slug='trier').delete()
    Belge.objects.filter(baslik='Miet-Angebotsbescheinigung — Kira Teklif Belgesi (Jobcenter 2025)', stadt__slug='mannheim').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0030_belgeler_mietbescheinigung'),
        ('stadt',  '0026_trier_aktiv'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
