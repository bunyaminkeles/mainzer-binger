"""
Düsseldorf şehri tam kurulum: Stadt güncelleme, Yerler ve Kaynaklar.
"""
from django.db import migrations

DUESSELDORF_YERLER = [
    {'kategori': 'resmi_kurum', 'ad': 'Ausländerbehörde Düsseldorf',      'adres': 'Willi-Becker-Allee 7, 40227 Düsseldorf',   'website': 'https://www.duesseldorf.de/auslaenderbehoerde', 'maps_url': 'https://maps.google.com/?q=Willi-Becker-Allee+7,+40227+D%C3%BCsseldorf'},
    {'kategori': 'resmi_kurum', 'ad': 'Jobcenter Düsseldorf',              'adres': 'Willi-Becker-Allee 15, 40227 Düsseldorf',  'website': 'https://www.jobcenter-duesseldorf.de',          'maps_url': 'https://maps.google.com/?q=Willi-Becker-Allee+15,+40227+D%C3%BCsseldorf'},
    {'kategori': 'resmi_kurum', 'ad': 'Agentur für Arbeit Düsseldorf',    'adres': 'Willi-Becker-Allee 15, 40227 Düsseldorf',  'website': 'https://www.arbeitsagentur.de/vor-ort/duesseldorf', 'maps_url': 'https://maps.google.com/?q=Willi-Becker-Allee+15,+40227+D%C3%BCsseldorf'},
    {'kategori': 'resmi_kurum', 'ad': 'Bürgeramt Düsseldorf — Stadtmitte','adres': 'Willi-Becker-Allee 7, 40227 Düsseldorf',   'website': 'https://www.duesseldorf.de/buergerbuero',       'maps_url': 'https://maps.google.com/?q=Willi-Becker-Allee+7,+40227+D%C3%BCsseldorf'},
    {'kategori': 'resmi_kurum', 'ad': 'Finanzamt Düsseldorf-Mitte',       'adres': 'Mühlenstr. 1, 40213 Düsseldorf',           'website': 'https://www.duesseldorf.de/finanzamt',          'maps_url': 'https://maps.google.com/?q=M%C3%BChlenstr.+1,+40213+D%C3%BCsseldorf'},
    {'kategori': 'saglik',      'ad': 'Universitätsklinikum Düsseldorf',  'adres': 'Moorenstr. 5, 40225 Düsseldorf',           'website': 'https://www.uniklinik-duesseldorf.de',          'maps_url': 'https://maps.google.com/?q=Moorenstr.+5,+40225+D%C3%BCsseldorf'},
    {'kategori': 'egitim',      'ad': 'Heinrich-Heine-Universität',       'adres': 'Universitätsstr. 1, 40225 Düsseldorf',     'website': 'https://www.hhu.de',                            'maps_url': 'https://maps.google.com/?q=Universit%C3%A4tsstr.+1,+40225+D%C3%BCsseldorf'},
    {'kategori': 'egitim',      'ad': 'VHS Düsseldorf — Volkshochschule', 'adres': 'Bertha-von-Suttner-Platz 1, 40227 Düsseldorf', 'website': 'https://www.vhs-duesseldorf.de',            'maps_url': 'https://maps.google.com/?q=Bertha-von-Suttner-Platz+1,+40227+D%C3%BCsseldorf'},
    {'kategori': 'ibadet',      'ad': 'DITIB Merkez Camii Düsseldorf',    'adres': 'Kruppstr. 7, 40227 Düsseldorf',            'website': 'https://ditib-duesseldorf.de',                  'maps_url': 'https://maps.google.com/?q=Kruppstr.+7,+40227+D%C3%BCsseldorf'},
    {'kategori': 'tuv',         'ad': 'TÜV Rheinland — Düsseldorf',       'adres': 'Am Grauen Stein 2, 51105 Köln',            'website': 'https://www.tuv.com/de/tuv-rheinland-gruppe/',  'maps_url': 'https://maps.google.com/?q=TÜV+Rheinland+Düsseldorf', 'aciklama': 'Araç muayenesi için en yakın TÜV Rheinland şubesini tuv.com üzerinden aratın.'},
    {'kategori': 'alisveris',   'ad': 'Königsallee (Kö)',                  'adres': 'Königsallee, 40212 Düsseldorf',            'website': 'https://www.koenigsallee.de',                   'maps_url': 'https://maps.google.com/?q=K%C3%B6nigsallee,+40212+D%C3%BCsseldorf', 'aciklama': 'Düsseldorf\'un lüks alışveriş caddesi.'},
    {'kategori': 'gezi',        'ad': 'Altstadt Düsseldorf',               'adres': 'Altstadt, 40213 Düsseldorf',               'website': 'https://www.duesseldorf.de/tourismus',          'maps_url': 'https://maps.google.com/?q=Altstadt,+40213+D%C3%BCsseldorf', 'aciklama': 'Dünyanın en uzun barının bulunduğu tarihi mahalle.'},
    {'kategori': 'gezi',        'ad': 'Kunstpalast Düsseldorf',            'adres': 'Ehrenhof 4-5, 40479 Düsseldorf',           'website': 'https://www.kunstpalast.de',                    'maps_url': 'https://maps.google.com/?q=Ehrenhof+4,+40479+D%C3%BCsseldorf'},
    {'kategori': 'turk_market', 'ad': 'Türk & Halal Marketler — Oberbilk','adres': 'Oberbilker Allee, 40227 Düsseldorf',       'website': '', 'maps_url': 'https://maps.google.com/?q=Oberbilker+Allee,+40227+D%C3%BCsseldorf', 'aciklama': 'Oberbilk mahallesi Türk marketleri ve helalcileri için en yoğun bölge.'},
]

DUESSELDORF_KAYNAKLAR = [
    {'kategori': 'resmi',  'baslik': 'Ausländerbehörde Düsseldorf',               'url': 'https://www.duesseldorf.de/auslaenderbehoerde',                          'ozet': 'Düsseldorf Yabancılar Dairesi; oturma izni, çalışma izni ve yabancı uyruklu diğer işlemler.',         'icon': 'bi-file-earmark-person-fill', 'sira': 1},
    {'kategori': 'resmi',  'baslik': 'Online Termin — Düsseldorf Belediyesi',     'url': 'https://termine.duesseldorf.de',                                         'ozet': 'Bürgeramt, Ausländerbehörde ve diğer belediye birimlerine online randevu.',                            'icon': 'bi-calendar-check-fill',      'sira': 2},
    {'kategori': 'is',     'baslik': 'Jobcenter Düsseldorf',                      'url': 'https://www.jobcenter-duesseldorf.de',                                   'ozet': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',                                  'icon': 'bi-briefcase-fill',           'sira': 3},
    {'kategori': 'is',     'baslik': 'Agentur für Arbeit Düsseldorf',             'url': 'https://www.arbeitsagentur.de/vor-ort/duesseldorf',                      'ozet': 'İşsizlik sigortası, mesleki rehberlik ve iş ilanları.',                                                  'icon': 'bi-person-workspace',         'sira': 4},
    {'kategori': 'konut',  'baslik': 'Düsseldorf KdU — Kosten der Unterkunft',   'url': 'https://www.duesseldorf.de/sozialamt/leistungen/grundsicherung-fuer-arbeitsuchende.html', 'ozet': '§ 22 SGB II kapsamında Düsseldorf\'ta Jobcenter tarafından karşılanan kira tavan değerleri.', 'icon': 'bi-house-fill', 'sira': 5},
    {'kategori': 'egitim', 'baslik': 'VHS Düsseldorf — Volkshochschule',          'url': 'https://www.vhs-duesseldorf.de',                                         'ozet': 'Almanca entegrasyon kursları, mesleki eğitim ve kültürel etkinlikler.',                                'icon': 'bi-translate',                'sira': 6},
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

    duesseldorf, _ = Stadt.objects.get_or_create(
        slug='duesseldorf',
        defaults={
            'eyalet': nw,
            'name': 'Düsseldorf',
            'typ': 'kreisfrei',
            'lat': 51.2256,
            'lng': 6.7767,
            'population': 645000,
            'beschreibung': 'Düsseldorf, Kuzey Ren-Vestfalya eyaletinin başkenti ve Almanya\'nın uluslararası iş merkezlerinden biridir.',
            'termin_url':            'https://termine.duesseldorf.de',
            'auslaenderbehorde_url': 'https://www.duesseldorf.de/auslaenderbehoerde',
            'rss_duyuru_url':        '',
            'aktiv': True,
        }
    )

    # Mevcut kayıt varsa URL'leri güncelle
    Stadt.objects.filter(slug='duesseldorf').update(
        termin_url='https://termine.duesseldorf.de',
        auslaenderbehorde_url='https://www.duesseldorf.de/auslaenderbehoerde',
        aktiv=True,
    )

    for v in DUESSELDORF_YERLER:
        Yer.objects.get_or_create(
            stadt=duesseldorf, ad=v['ad'],
            defaults={
                'kategori': v['kategori'],
                'adres':    v['adres'],
                'website':  v.get('website', ''),
                'maps_url': v.get('maps_url', ''),
                'aciklama': v.get('aciklama', ''),
                'sehir': 'Düsseldorf', 'scope': 'stadt', 'tur': 'yer', 'aktif': True,
            }
        )

    for d in DUESSELDORF_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=duesseldorf,
            defaults={**d, 'eyalet': nw, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='duesseldorf').update(
        termin_url='', auslaenderbehorde_url='', aktiv=False
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0028_bad_kreuznach_aktiv'),
        ('yerler', '0001_initial'),
        ('rehber', '0034_yeni_belgeler_ekle'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
