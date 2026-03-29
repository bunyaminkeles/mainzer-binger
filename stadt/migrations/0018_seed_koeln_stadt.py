"""
Köln Stadt objesi Hetzner'de eksikti — 0016/0017/0027 migration'ları
Stadt.DoesNotExist ile sessizce atlamıştı. Bu migration her şeyi tek seferde kurar.
"""
from django.db import migrations

KOELN_YERLER = [
    {'kategori': 'resmi_kurum', 'ad': 'Ausländerbehörde Köln',        'adres': 'Ossendorfweg 35, 50829 Köln',           'website': 'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt', 'maps_url': 'https://maps.google.com/?q=Ossendorfweg+35,+50829+K%C3%B6ln'},
    {'kategori': 'resmi_kurum', 'ad': 'Jobcenter Köln',               'adres': 'Bartholomäus-Schink-Str. 6, 50825 Köln','website': 'https://jobcenter.digital/koeln',                              'maps_url': 'https://maps.google.com/?q=Bartholom%C3%A4us-Schink-Str.+6,+50825+K%C3%B6ln'},
    {'kategori': 'resmi_kurum', 'ad': 'Agentur für Arbeit Köln',      'adres': 'Luxemburger Str. 121, 50939 Köln',      'website': 'https://www.arbeitsagentur.de/vor-ort/koeln',                  'maps_url': 'https://maps.google.com/?q=Luxemburger+Str.+121,+50939+K%C3%B6ln'},
    {'kategori': 'resmi_kurum', 'ad': 'Finanzamt Köln-Mitte',         'adres': 'Breite Str. 3-5, 50667 Köln',           'website': 'https://www.finanzamt.nrw.de/finanzaemter/koeln-mitte',        'maps_url': 'https://maps.google.com/?q=Breite+Str.+3,+50667+K%C3%B6ln'},
    {'kategori': 'resmi_kurum', 'ad': 'KFZ-Zulassungsstelle Köln',    'adres': 'Neusser Str. 105, 50670 Köln',          'website': 'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt','maps_url': 'https://maps.google.com/?q=Neusser+Str.+105,+50670+K%C3%B6ln'},
    {'kategori': 'saglik',      'ad': 'Universitätsklinikum Köln',    'adres': 'Kerpener Str. 62, 50937 Köln',          'website': 'https://www.uk-koeln.de',                                      'maps_url': 'https://maps.google.com/?q=Kerpener+Str.+62,+50937+K%C3%B6ln'},
    {'kategori': 'egitim',      'ad': 'Universität zu Köln',          'adres': 'Albertus-Magnus-Platz, 50923 Köln',     'website': 'https://www.uni-koeln.de',                                     'maps_url': 'https://maps.google.com/?q=Albertus-Magnus-Platz,+50923+K%C3%B6ln'},
    {'kategori': 'egitim',      'ad': 'VHS Köln — Volkshochschule',   'adres': 'Ottoplatz 2, 50679 Köln',               'website': 'https://www.vhs-koeln.de',                                     'maps_url': 'https://maps.google.com/?q=Ottoplatz+2,+50679+K%C3%B6ln'},
    {'kategori': 'ibadet',      'ad': 'DITIB Zentralmoschee Köln',    'adres': 'Venloer Str. 160, 50823 Köln',          'website': 'https://www.zentralmoschee-koeln.de',                          'maps_url': 'https://maps.google.com/?q=Venloer+Str.+160,+50823+K%C3%B6ln'},
    {'kategori': 'tuv',         'ad': 'TÜV Rheinland — Köln',         'adres': 'Am Grauen Stein 2, 51105 Köln',         'website': 'https://www.tuv.com/de/tuv-rheinland-gruppe/',                 'maps_url': 'https://maps.google.com/?q=Am+Grauen+Stein+2,+51105+K%C3%B6ln'},
    {'kategori': 'alisveris',   'ad': 'Rhein-Center Köln',            'adres': 'Aachener Str. 1253, 50858 Köln',        'website': 'https://www.rheincenter.de',                                   'maps_url': 'https://maps.google.com/?q=Aachener+Str.+1253,+50858+K%C3%B6ln'},
    {'kategori': 'gezi',        'ad': 'Kölner Dom',                   'adres': 'Domkloster 4, 50667 Köln',              'website': 'https://www.koelner-dom.de',                                   'maps_url': 'https://maps.google.com/?q=Domkloster+4,+50667+K%C3%B6ln',       'aciklama': 'UNESCO Dünya Mirası listesinde yer alan Gotik katederal.'},
    {'kategori': 'gezi',        'ad': 'Köln Müzesi Kompleksi',        'adres': 'Roncalliplatz 4, 50667 Köln',           'website': 'https://www.museenkoeln.de',                                   'maps_url': 'https://maps.google.com/?q=Roncalliplatz+4,+50667+K%C3%B6ln'},
    {'kategori': 'turk_market', 'ad': 'Türk & Halal Marketler — Ehrenfeld', 'adres': 'Venloer Str. / Ehrenfeld, 50823 Köln', 'website': '', 'maps_url': 'https://maps.google.com/?q=Venloer+Str.,+50823+K%C3%B6ln', 'aciklama': 'Ehrenfeld mahallesi Türk marketleri ve helalcileri için en yoğun bölge.'},
]

KOELN_KAYNAKLAR = [
    {'kategori': 'resmi',  'baslik': 'Ausländerbehörde Köln',              'url': 'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt',               'ozet': 'Köln Yabancılar Dairesi; oturma izni, çalışma izni ve yabancı uyruklu diğer işlemler.',  'icon': 'bi-file-earmark-person-fill', 'sira': 1},
    {'kategori': 'resmi',  'baslik': 'Terminvereinbarung — Köln Online Randevu', 'url': 'https://www.stadt-koeln.de/service/kontakt/terminvereinbarung-online',   'ozet': 'Stadt Köln belediye birimlerine online randevu; Bürgerbüro, Ausländerbehörde ve diğerleri.', 'icon': 'bi-calendar-check-fill',     'sira': 2},
    {'kategori': 'is',     'baslik': 'Jobcenter Köln',                     'url': 'https://jobcenter.digital/koeln',                                               'ozet': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',                       'icon': 'bi-briefcase-fill',           'sira': 3},
    {'kategori': 'is',     'baslik': 'Agentur für Arbeit Köln',            'url': 'https://www.arbeitsagentur.de/vor-ort/koeln',                                   'ozet': 'İşsizlik sigortası, mesleki rehberlik ve iş ilanları.',                                      'icon': 'bi-person-workspace',         'sira': 4},
    {'kategori': 'konut',  'baslik': 'Köln KdU — Kosten der Unterkunft Bilgisi', 'url': 'https://www.stadt-koeln.de/service/anliegen/sozialleistungen-wohnen',    'ozet': '§ 22 SGB II kapsamında Köln\'de Jobcenter tarafından karşılanan kira tavan değerleri.',   'icon': 'bi-house-fill',               'sira': 5},
    {'kategori': 'egitim', 'baslik': 'VHS Köln — Volkshochschule',         'url': 'https://www.vhs-koeln.de',                                                     'ozet': 'Almanca entegrasyon kursları, mesleki eğitim ve kültürel etkinlikler.',                     'icon': 'bi-translate',                'sira': 6},
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    Kaynak = apps.get_model('rehber', 'Kaynak')

    try:
        nw = Eyalet.objects.get(kod='NW')
    except Eyalet.DoesNotExist:
        return

    koeln, _ = Stadt.objects.get_or_create(
        slug='koeln',
        defaults={
            'eyalet': nw,
            'name': 'Köln',
            'typ': 'kreisfrei',
            'lat': 50.9333,
            'lng': 6.9500,
            'population': 1084394,
            'beschreibung': 'Köln, Almanya\'nın Nordrhein-Westfalen eyaletinde bulunan bir şehirdir. Nüfusu 1 milyonun üzerindedir ve Almanya\'nın dördüncü en büyük şehridir.',
            'termin_url':            'https://www.stadt-koeln.de/service/kontakt/terminvereinbarung-online',
            'auslaenderbehorde_url': 'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt',
            'rss_duyuru_url':        '',
            'aktiv': True,
        }
    )

    for v in KOELN_YERLER:
        Yer.objects.get_or_create(
            stadt=koeln, ad=v['ad'],
            defaults={
                'kategori': v['kategori'],
                'adres':    v['adres'],
                'website':  v.get('website', ''),
                'maps_url': v.get('maps_url', ''),
                'aciklama': v.get('aciklama', ''),
                'sehir': 'Köln', 'scope': 'stadt', 'tur': 'yer', 'aktif': True,
            }
        )

    for d in KOELN_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=koeln,
            defaults={**d, 'eyalet': nw, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='koeln').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0017_fix_rss_urls'),
        ('yerler', '0001_initial'),
        ('rehber', '0027_seed_koeln_kaynaklar'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
