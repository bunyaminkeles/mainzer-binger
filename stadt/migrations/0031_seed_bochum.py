"""
Bochum şehri tam kurulum: Stadt kaydı, Yerler ve Kaynaklar.
"""
from django.db import migrations

BOCHUM_YERLER = [
    # Resmi Kurumlar
    {'kategori': 'resmi_kurum', 'ad': 'Ausländerbehörde Bochum',           'adres': 'Willy-Brandt-Platz 2–6, 44787 Bochum',       'website': 'https://www.bochum.de/Stadtamt/Auslaenderbehoerde',            'maps_url': 'https://maps.google.com/?q=Ausländerbehörde+Bochum+Willy-Brandt-Platz'},
    {'kategori': 'resmi_kurum', 'ad': 'Jobcenter Bochum',                  'adres': 'Ostring 30, 44787 Bochum',                    'website': 'https://www.jobcenter-bochum.de',                              'maps_url': 'https://maps.google.com/?q=Jobcenter+Bochum+Ostring+30'},
    {'kategori': 'resmi_kurum', 'ad': 'Agentur für Arbeit Bochum',         'adres': 'Ostring 30, 44787 Bochum',                    'website': 'https://www.arbeitsagentur.de/vor-ort/bochum',                'maps_url': 'https://maps.google.com/?q=Agentur+für+Arbeit+Bochum+Ostring'},
    {'kategori': 'resmi_kurum', 'ad': 'Bürger-Service-Center Bochum',      'adres': 'Willy-Brandt-Platz 2–6, 44787 Bochum',       'website': 'https://www.bochum.de/Stadtamt/Buergerservice',               'maps_url': 'https://maps.google.com/?q=Bürger-Service-Center+Bochum'},
    {'kategori': 'resmi_kurum', 'ad': 'Finanzamt Bochum-Mitte',            'adres': 'Springerstr. 4–10, 44789 Bochum',             'website': 'https://www.finanzverwaltung.nrw.de',                         'maps_url': 'https://maps.google.com/?q=Finanzamt+Bochum+Mitte+Springerstr'},
    # Sağlık
    {'kategori': 'saglik',      'ad': 'Knappschaftskrankenhaus Bochum',    'adres': 'In der Schornau 23–25, 44892 Bochum',         'website': 'https://www.kk-bochum.de',                                    'maps_url': 'https://maps.google.com/?q=Knappschaftskrankenhaus+Bochum'},
    {'kategori': 'saglik',      'ad': 'St. Josef Hospital Bochum',         'adres': 'Gudrunstr. 56, 44791 Bochum',                 'website': 'https://www.klinikum-bochum.de',                              'maps_url': 'https://maps.google.com/?q=St+Josef+Hospital+Bochum'},
    # Eğitim
    {'kategori': 'egitim',      'ad': 'Ruhr-Universität Bochum (RUB)',     'adres': 'Universitätsstr. 150, 44801 Bochum',          'website': 'https://www.ruhr-uni-bochum.de',                              'maps_url': 'https://maps.google.com/?q=Ruhr-Universität+Bochum'},
    {'kategori': 'egitim',      'ad': 'VHS Bochum — Volkshochschule',      'adres': 'Huestr. 5, 44787 Bochum',                    'website': 'https://www.vhs-bochum.de',                                   'maps_url': 'https://maps.google.com/?q=VHS+Bochum+Huestr'},
    # İbadet
    {'kategori': 'ibadet',      'ad': 'DITIB Türkisch-Islamische Gemeinde Bochum', 'adres': 'Herner Str. 45, 44787 Bochum',       'website': 'https://www.ditib.de',                                        'maps_url': 'https://maps.google.com/?q=DITIB+Bochum+Herner+Str'},
    {'kategori': 'ibadet',      'ad': 'Islamisches Zentrum Bochum (IGMG)', 'adres': 'Castroper Str. 228, 44805 Bochum',            'website': 'https://www.igmg.org',                                        'maps_url': 'https://maps.google.com/?q=Islamisches+Zentrum+Bochum+IGMG'},
    # TÜV / Araç muayene
    {'kategori': 'tuv',         'ad': 'DEKRA Automobil Bochum',            'adres': 'Industriestr. 13–15, 44866 Bochum',           'website': 'https://www.dekra.de',                                        'maps_url': 'https://maps.google.com/?q=DEKRA+Bochum+Industriestr'},
    {'kategori': 'tuv',         'ad': 'TÜV Nord — Bochum',                 'adres': 'Am Technologiezentrum 1, 44807 Bochum',       'website': 'https://www.tuev-nord.de',                                    'maps_url': 'https://maps.google.com/?q=TÜV+Nord+Bochum', 'aciklama': 'Araç muayenesi (HU/AU) ve teknik incelemeler.'},
    # Alışveriş
    {'kategori': 'alisveris',   'ad': 'Ruhr Park Bochum',                  'adres': 'Am Ruhr Park 1, 44791 Bochum',                'website': 'https://www.ruhrpark.de',                                     'maps_url': 'https://maps.google.com/?q=Ruhr+Park+Bochum', 'aciklama': 'Bochum\'un en büyük alışveriş ve eğlence merkezi.'},
    {'kategori': 'alisveris',   'ad': 'Bochum Innenstadt (Kortumstraße)',  'adres': 'Kortumstraße, 44787 Bochum',                  'website': '',                                                            'maps_url': 'https://maps.google.com/?q=Kortumstraße+Bochum', 'aciklama': 'Bochum şehir merkezinin ana yaya alışveriş caddesi.'},
    # Gezi & Kültür
    {'kategori': 'gezi',        'ad': 'Deutsches Bergbau-Museum Bochum',   'adres': 'Am Bergbaumuseum 28, 44791 Bochum',           'website': 'https://www.bergbaumuseum.de',                                'maps_url': 'https://maps.google.com/?q=Deutsches+Bergbau-Museum+Bochum', 'aciklama': 'Dünyanın en büyük madencilik müzesi. Bochum\'un simge yapısı.'},
    {'kategori': 'gezi',        'ad': 'Zeiss Planetarium Bochum',          'adres': 'Castroper Str. 67, 44791 Bochum',             'website': 'https://www.planetarium-bochum.de',                          'maps_url': 'https://maps.google.com/?q=Zeiss+Planetarium+Bochum', 'aciklama': 'Almanya\'nın en eski hâlâ açık planetaryumu.'},
]

BOCHUM_KAYNAKLAR = [
    {'kategori': 'resmi',  'baslik': 'Ausländerbehörde Bochum',               'url': 'https://www.bochum.de/Stadtamt/Auslaenderbehoerde',                              'ozet': 'Bochum Yabancılar Dairesi; oturma izni, çalışma izni ve yabancı uyruklu diğer işlemler.',          'icon': 'bi-file-earmark-person-fill', 'sira': 1},
    {'kategori': 'resmi',  'baslik': 'Online Termin — Bochum Belediyesi',     'url': 'https://www.bochum.de/Stadtamt/Online-Services/Terminreservierung',              'ozet': 'Bürger-Service-Center ve diğer belediye birimlerine online randevu.',                              'icon': 'bi-calendar-check-fill',      'sira': 2},
    {'kategori': 'is',     'baslik': 'Jobcenter Bochum',                      'url': 'https://www.jobcenter-bochum.de',                                                 'ozet': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',                              'icon': 'bi-briefcase-fill',           'sira': 3},
    {'kategori': 'is',     'baslik': 'Agentur für Arbeit Bochum',             'url': 'https://www.arbeitsagentur.de/vor-ort/bochum',                                   'ozet': 'İşsizlik sigortası, mesleki rehberlik ve iş ilanları.',                                            'icon': 'bi-person-workspace',         'sira': 4},
    {'kategori': 'konut',  'baslik': 'Bochum KdU — Kosten der Unterkunft',   'url': 'https://www.bochum.de/Stadtamt/Sozialamt/Grundsicherung-fuer-Arbeitsuchende',    'ozet': '§ 22 SGB II kapsamında Bochum\'da Jobcenter tarafından karşılanan kira tavan değerleri.',         'icon': 'bi-house-fill',               'sira': 5},
    {'kategori': 'egitim', 'baslik': 'VHS Bochum — Volkshochschule',          'url': 'https://www.vhs-bochum.de',                                                      'ozet': 'Almanca entegrasyon kursları, mesleki eğitim ve kültürel etkinlikler.',                            'icon': 'bi-translate',                'sira': 6},
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

    bochum, _ = Stadt.objects.get_or_create(
        slug='bochum',
        defaults={
            'eyalet': nw,
            'name': 'Bochum',
            'typ': 'kreisfrei',
            'lat': 51.4818,
            'lng': 7.2162,
            'population': 365000,
            'beschreibung': 'Bochum, Kuzey Ren-Vestfalya eyaletinde, Ruhr bölgesinin kalbinde yer alan sanayi ve kültür şehridir. Ruhr Üniversitesi ve Alman Madencilik Müzesi ile tanınır.',
            'termin_url':            'https://www.bochum.de/Stadtamt/Online-Services/Terminreservierung',
            'auslaenderbehorde_url': 'https://www.bochum.de/Stadtamt/Auslaenderbehoerde',
            'rss_duyuru_url':        'https://www.bochum.de/Presse/Pressemitteilungen',
            'aktiv': True,
        }
    )

    # Mevcut kayıt varsa URL'leri ve aktifliği güncelle
    Stadt.objects.filter(slug='bochum').update(
        termin_url='https://www.bochum.de/Stadtamt/Online-Services/Terminreservierung',
        auslaenderbehorde_url='https://www.bochum.de/Stadtamt/Auslaenderbehoerde',
        rss_duyuru_url='https://www.bochum.de/Presse/Pressemitteilungen',
        aktiv=True,
    )

    for v in BOCHUM_YERLER:
        Yer.objects.get_or_create(
            stadt=bochum, ad=v['ad'],
            defaults={
                'kategori': v['kategori'],
                'adres':    v['adres'],
                'website':  v.get('website', ''),
                'maps_url': v.get('maps_url', ''),
                'aciklama': v.get('aciklama', ''),
                'sehir': 'Bochum', 'scope': 'stadt', 'tur': 'yer', 'aktif': True,
                'eyalet': nw,
            }
        )

    for d in BOCHUM_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=bochum,
            defaults={**d, 'eyalet': nw, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='bochum').update(
        termin_url='', auslaenderbehorde_url='', rss_duyuru_url='', aktiv=False
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0030_fix_duesseldorf_auslaenderamt_url'),
        ('yerler', '0001_initial'),
        ('rehber', '0034_yeni_belgeler_ekle'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
