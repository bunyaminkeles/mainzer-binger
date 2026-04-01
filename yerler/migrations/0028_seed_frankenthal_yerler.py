from django.db import migrations

IBADET = [
    {
        'ad': 'DITIB Kocatepe Camii Frankenthal',
        'adres': 'Mörscher Str. 97, 67227 Frankenthal',
        'aciklama': 'Frankenthal bölgesindeki en büyük Türk-İslam camii. Cuma namazı, Kuran kursu ve sosyal etkinlikler düzenlenmektedir.',
        'website': 'https://www.ditib.de',
        'maps_url': 'https://maps.google.com/?q=DITIB+Kocatepe+Camii+Frankenthal',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'IGMG Frankenthal',
        'adres': 'Schraderstraße 1, 67227 Frankenthal',
        'aciklama': 'İslam Toplumu Millî Görüş (IGMG) bünyesinde hizmet veren cami ve eğitim merkezi.',
        'website': 'https://www.igmg.org',
        'maps_url': 'https://maps.google.com/?q=IGMG+Frankenthal',
        'kapak_resmi': '',
        'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV Rheinland Prüfstelle Frankenthal',
        'adres': 'Mahlastraße 102, 67227 Frankenthal',
        'aciklama': 'TÜV Rheinland araç muayene istasyonu. HU/AU periyodik muayenesi ve teknik incelemeler yapılmaktadır.',
        'website': 'https://www.tuv.com',
        'maps_url': 'https://maps.google.com/?q=TÜV+Rheinland+Frankenthal+Mahlastraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'DEKRA Automobil Station Frankenthal',
        'adres': 'Beindersheimer Str. 79, 67227 Frankenthal',
        'aciklama': 'DEKRA araç muayene ve ekspertiz merkezi. Randevusuz veya randevulu muayene imkanı.',
        'website': 'https://www.dekra.de',
        'maps_url': 'https://maps.google.com/?q=DEKRA+Frankenthal+Beindersheimer',
        'kapak_resmi': '',
        'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'Stadtklinik Frankenthal',
        'adres': 'Elsa-Brändström-Straße 1, 67227 Frankenthal',
        'aciklama': 'Frankenthal şehir hastanesi. Acil servis, dahiliye, cerrahi ve psikiyatri bölümleriyle 24 saat hizmet vermektedir.',
        'website': 'https://www.stadtklinik-ft.de',
        'maps_url': 'https://maps.google.com/?q=Stadtklinik+Frankenthal',
        'kapak_resmi': '',
        'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'vhs Frankenthal — Volkshochschule',
        'adres': 'Schlossergasse 8, 67227 Frankenthal',
        'aciklama': 'Frankenthal Halk Eğitim Merkezi. Almanca dil kursları, BAMF entegrasyon eğitimleri ve mesleki programlar verilmektedir.',
        'website': 'https://www.vhs-ft.de',
        'maps_url': 'https://maps.google.com/?q=vhs+Frankenthal+Schlossergasse',
        'kapak_resmi': '',
        'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'Frankenthal Innenstadt (Einkaufsmeile)',
        'adres': 'Speyerer Straße / Bahnhofstraße, 67227 Frankenthal',
        'aciklama': 'Frankenthal şehir merkezi. Giyim, kozmetik mağazaları (H&M, dm vb.), kafeler ve haftalık açık pazarın bulunduğu yaya bölgesi.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Speyerer+Straße+Frankenthal',
        'kapak_resmi': '',
        'icerik': '',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='RP')
        frankenthal = Stadt.objects.get(slug='frankenthal')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    kategoriler = [
        ('ibadet', IBADET),
        ('tuv', TUV),
        ('saglik', SAGLIK),
        ('egitim', EGITIM),
        ('alisveris', ALISVERIS),
    ]

    for kategori_slug, yerler in kategoriler:
        for veri in yerler:
            Yer.objects.get_or_create(
                ad=veri['ad'],
                stadt=frankenthal,
                defaults={
                    'eyalet': eyalet,
                    'scope': 'stadt',
                    'tur': 'yer',
                    'kategori': kategori_slug,
                    'adres': veri['adres'],
                    'sehir': 'Frankenthal',
                    'aciklama': veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''),
                    'website': veri.get('website', ''),
                    'maps_url': veri.get('maps_url', ''),
                    'icerik': veri.get('icerik', ''),
                    'aktif': True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = (
        [v['ad'] for v in IBADET] +
        [v['ad'] for v in TUV] +
        [v['ad'] for v in SAGLIK] +
        [v['ad'] for v in EGITIM] +
        [v['ad'] for v in ALISVERIS]
    )
    Yer.objects.filter(ad__in=adlar, sehir='Frankenthal').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0027_seed_ludwigshafen_yerler'),
        # Eğer Frankenthal'in aktivasyonu stadt altında bir migration'a bağlıysa
        # ('stadt', '00XX_frankenthal_aktiv') buraya eklenebilir.
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]