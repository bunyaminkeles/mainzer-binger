"""
Belge havuzu — SADECE doğrudan indirilebilir PDF/DOCX dosyalar.
Bilgi sayfaları veya web portalları bu modele EKLENMEMELİDİR.
"""
from django.db import migrations

FEDERAL_BELGELER = [
    {
        'baslik': 'Kindergeld Ana Başvuru Formu (KG1)',
        'kategori': 'aile',
        'harici_link': 'https://www.arbeitsagentur.de/datei/kg1-antrag-kindergeld_ba043063.pdf',
        'ozet': 'Çocuk parası (Kindergeld) için resmi başvuru formu.',
    },
    {
        'baslik': 'Kindergeld — Banka Hesap Değişikliği (KG105)',
        'kategori': 'aile',
        'harici_link': 'https://www.arbeitsagentur.de/datei/kg105-aenderung-bankverbindung_ba013533.pdf',
        'ozet': 'Kindergeld ödemelerinin aktarılacağı banka hesabını değiştirme formu.',
    },
    {
        'baslik': 'Elterngeld Başvuru Formu',
        'kategori': 'aile',
        'harici_link': 'https://www.arbeitsagentur.de/datei/elterngeld-antrag_ba036071.pdf',
        'ozet': 'Doğum sonrası ebeveyn yardımı (Elterngeld) başvuru formu.',
    },
    {
        'baslik': 'SEPA Otomatik Ödeme Talimatı (Lastschriftmandat)',
        'kategori': 'genel',
        'harici_link': 'https://www.arbeitsagentur.de/datei/sepa-lastschriftmandat_ba014022.pdf',
        'ozet': 'Kurumlarla otomatik ödeme talimatı vermek için SEPA formu.',
    },
    {
        'baslik': 'Wohnungsgeberbestätigung — Ev Sahibi Onay Belgesi (Federal Şablon)',
        'kategori': 'konut',
        'harici_link': 'https://www.bundesregierung.de/resource/blob/974430/2185598/wohnungsgeberbestaetigung_muster.pdf',
        'ozet': 'İkametgah kaydı için ev sahibinden alınacak onay belgesi şablonu.',
    },
    {
        'baslik': 'Vollmacht — Genel Vekaletname Şablonu',
        'kategori': 'genel',
        'harici_link': 'https://www.bundesjustizamt.de/SharedDocs/Downloads/DE/Formulare/Vollmacht.pdf',
        'ozet': 'Resmi işlemlerde kullanılabilecek genel vekaletname formu.',
    },
]

MAINZ_BELGELER = [
    {
        'baslik': 'Wohnungsgeberbestätigung (Ev Sahibi Onay Belgesi) — Mainz',
        'kategori': 'konut',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Wohnungsgeberbestaetigung.pdf',
        'ozet': 'Mainz Bürgerbüro için ev sahibinden alınacak ikamet onay formu.',
    },
    {
        'baslik': 'Aufenthaltserlaubnis — Oturum İzni Başvuru Formu (Mainz)',
        'kategori': 'vize',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Aufenthaltserlaubnis-Antrag-Erteilung-Verlaengerung.pdf',
        'ozet': 'Mainz Ausländerbehörde oturum izni başvurusu ve uzatma formu.',
    },
    {
        'baslik': 'Vollmacht Kfz-Zulassung — Araç Kayıt Vekaletnamesi (Mainz)',
        'kategori': 'genel',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Vollmacht-Kfz-Zulassung.pdf',
        'ozet': 'Mainz araç tescili için başkasına verilebilecek vekaletname formu.',
    },
]


def seed(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    Stadt = apps.get_model('stadt', 'Stadt')

    for d in FEDERAL_BELGELER:
        Belge.objects.get_or_create(
            baslik=d['baslik'],
            stadt=None,
            defaults={
                'kategori':    d['kategori'],
                'harici_link': d['harici_link'],
                'ozet':        d.get('ozet', ''),
                'yayinda':     True,
            }
        )

    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    for d in MAINZ_BELGELER:
        Belge.objects.get_or_create(
            baslik=d['baslik'],
            stadt=mainz,
            defaults={
                'kategori':    d['kategori'],
                'harici_link': d['harici_link'],
                'ozet':        d.get('ozet', ''),
                'yayinda':     True,
            }
        )


def unseed(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    federal_basliklar = [d['baslik'] for d in FEDERAL_BELGELER]
    mainz_basliklar   = [d['baslik'] for d in MAINZ_BELGELER]
    Belge.objects.filter(baslik__in=federal_basliklar, stadt__isnull=True).delete()
    Belge.objects.filter(baslik__in=mainz_basliklar, stadt__slug='mainz').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0028_belge_modeli'),
        ('stadt',  '0018_seed_koeln_stadt'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
