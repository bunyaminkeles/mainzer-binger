from django.db import migrations

IBADET = [
    {
        'ad': 'DITIB Merkez Camii Ludwigshafen',
        'adres': 'Lisztstraße 8, 67063 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen\'ın en büyük camii olup DITIB bünyesinde faaliyet göstermektedir. Beş vakit namaz, Kuran kursları, cenaze hizmetleri ve çeşitli sosyal etkinlikler düzenlenmektedir.',
        'website': 'https://www.ditib.de',
        'maps_url': 'https://maps.google.com/?q=DITIB+Merkez+Camii+Ludwigshafen+Lisztstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'IGMG Mevlana Camii Ludwigshafen',
        'adres': 'Sternstraße 19, 67063 Ludwigshafen am Rhein',
        'aciklama': 'İslam Toplumu Millî Görüş (IGMG) bünyesindeki Mevlana Camii. Cuma namazı, Kuran eğitimi, gençlik programları ve aile danışmanlığı hizmetleri sunulmaktadır.',
        'website': 'https://www.igmg.org',
        'maps_url': 'https://maps.google.com/?q=IGMG+Mevlana+Camii+Ludwigshafen+Sternstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Islamisches Zentrum Ludwigshafen',
        'adres': 'Mundenheimer Str. 12, 67061 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen\'daki çok toplumlu İslam kültür merkezi. Beş vakit namaz, Kuran öğretimi ve Türkçe-Almanca sosyal danışmanlık hizmetleri sunulmaktadır.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Islamisches+Zentrum+Ludwigshafen+Mundenheimer',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Ahmadiyya Muslim Jamaat — Ludwigshafen',
        'adres': 'Heinigstraße 55, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Ahmadiyya Müslüman cemaatine ait ibadet merkezi. Günlük namazlar, dini toplantılar ve diyalog etkinlikleri düzenlenmektedir.',
        'website': 'https://www.ahmadiyya.de',
        'maps_url': 'https://maps.google.com/?q=Ahmadiyya+Muslim+Jamaat+Ludwigshafen+Heinigstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV Rheinland Kfz-Prüfstelle Ludwigshafen',
        'adres': 'Brunckstraße 47, 67063 Ludwigshafen am Rhein',
        'aciklama': 'TÜV Rheinland\'ın Ludwigshafen araç muayene merkezi. HU (Hauptuntersuchung) ve AU (Abgasuntersuchung) başta olmak üzere çeşitli teknik kontroller yapılmaktadır. Online randevu alınabilmektedir.',
        'website': 'https://www.tuv.com/deutschland/de/hauptuntersuchung.html',
        'maps_url': 'https://maps.google.com/?q=TÜV+Rheinland+Ludwigshafen+Brunckstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'DEKRA Automobil Station Ludwigshafen',
        'adres': 'Industriestraße 34, 67063 Ludwigshafen am Rhein',
        'aciklama': 'DEKRA\'nın Ludwigshafen araç muayene merkezi. HU, AU ve araç değerleme hizmetlerinin yanı sıra teknik ekspertiz ve hasar tespiti hizmetleri de sunulmaktadır.',
        'website': 'https://www.dekra.de',
        'maps_url': 'https://maps.google.com/?q=DEKRA+Automobil+Station+Ludwigshafen+Industriestraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'GTÜ Kfz-Prüfstelle Ludwigshafen-Mitte',
        'adres': 'Rohrlachstraße 42, 67061 Ludwigshafen am Rhein',
        'aciklama': 'GTÜ (Gesellschaft für Technische Überwachung) muayene istasyonu. TÜV ve DEKRA\'ya alternatif olarak araç periyodik muayenesi (HU/AU) yapılmakta olup uygun fiyatlı hizmet sunulmaktadır.',
        'website': 'https://www.gtue.de',
        'maps_url': 'https://maps.google.com/?q=GTÜ+Kfz-Prüfstelle+Ludwigshafen+Rohrlachstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'Klinikum der Stadt Ludwigshafen',
        'adres': 'Bremserstraße 79, 67063 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen\'ın ana hastanesi. 1.000\'den fazla yatak kapasitesiyle 20\'den fazla klinik ve enstitüde acil servis, dahiliye, cerrahi, kardiyoloji ve birçok uzmanlık dalında 24 saat hizmet vermektedir.',
        'website': 'https://www.klinikum-lu.de',
        'maps_url': 'https://maps.google.com/?q=Klinikum+Stadt+Ludwigshafen+Bremserstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'St. Marienkrankenhaus Ludwigshafen',
        'adres': 'Salzburger Str. 15, 67067 Ludwigshafen am Rhein',
        'aciklama': 'Katolik kilisesi bünyesindeki St. Marienkrankenhaus. Cerrahi, ortopedi, kadın doğum ve nöroloji başta olmak üzere birçok uzmanlık dalında hizmet veren köklü bir hastanedir.',
        'website': 'https://www.st-marienkrankenhaus.de',
        'maps_url': 'https://maps.google.com/?q=St.+Marienkrankenhaus+Ludwigshafen+Salzburger+Str',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Ärztlicher Bereitschaftsdienst — 116 117 (Ludwigshafen)',
        'adres': 'Bremserstraße 79, 67063 Ludwigshafen am Rhein',
        'aciklama': 'KV RLP\'nin acil nöbet hattı. Hafta sonu ve gece saatlerinde acil olmayan sağlık sorunları için 116 117 numarası aranarak Klinikum LU\'daki nöbet pratiğine yönlendirme alınabilir.',
        'website': 'https://www.kv-rlp.de/patienten/patientenservice-116117',
        'maps_url': '',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Gesundheitsamt Ludwigshafen',
        'adres': 'Röntgenstraße 8, 67063 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen Sağlık Dairesi. Aşılama, bulaşıcı hastalık bildirimi, çocuk sağlığı taramaları ve göçmen sağlık danışmanlığı hizmetleri sunulmaktadır.',
        'website': 'https://www.ludwigshafen.de/buergerservice/gesundheitsamt/',
        'maps_url': 'https://maps.google.com/?q=Gesundheitsamt+Ludwigshafen+Röntgenstraße',
        'kapak_resmi': '',
        'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'vhs Ludwigshafen — Volkshochschule',
        'adres': 'Bürgerhof 2, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen Halk Eğitim Merkezi. Almanca dil kursları (A1–C2), BAMF entegrasyon kursları, mesleki eğitim, dijital okuryazarlık ve kültürel programlar sunulmaktadır.',
        'website': 'https://www.vhs-lu.de',
        'maps_url': 'https://maps.google.com/?q=vhs+Ludwigshafen+Volkshochschule+Bürgerhof',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Hochschule Ludwigshafen am Rhein',
        'adres': 'Ernst-Boehe-Str. 4, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen Uygulamalı Bilimler Üniversitesi. İşletme, sosyal hizmetler, sağlık yönetimi ve diyetetik alanlarında yaklaşık 4.000 öğrenciye yönelik lisans ve yüksek lisans programları sunulmaktadır.',
        'website': 'https://www.hwg-lu.de',
        'maps_url': 'https://maps.google.com/?q=Hochschule+Ludwigshafen+am+Rhein+Ernst-Boehe-Str',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Bildungszentrum Ludwigshafen — BASF',
        'adres': 'Carl-Bosch-Str., 67056 Ludwigshafen am Rhein',
        'aciklama': 'Dünyanın en büyük kimya şirketi BASF\'ın mesleki eğitim merkezi. Şehirdeki kimya, lojistik ve teknik alanlarda çıraklık ve mesleki eğitim programları sunmaktadır.',
        'website': 'https://www.basf.com/de/ausbildung',
        'maps_url': 'https://maps.google.com/?q=BASF+Ludwigshafen+Bildungszentrum',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'BAMF-NAvI — Integrationskurs Ludwigshafen',
        'adres': 'Telefonla erişim / Online',
        'aciklama': 'BAMF entegrasyon kursu rehberi. Ludwigshafen ve çevresindeki yetkili kurs merkezlerini, kurs haklarını ve başvuru sürecini adım adım açıklar.',
        'website': 'https://bamf-navi.bamf.de',
        'maps_url': '',
        'kapak_resmi': '',
        'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'Rhein-Galerie Ludwigshafen',
        'adres': 'Bahnhofstr. 1, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Ren kıyısında yer alan modern alışveriş merkezi. 120\'den fazla mağaza, restoranlar ve hizmet noktaları ile şehrin en büyük alışveriş kompleksidir. Ücretsiz otopark mevcuttur.',
        'website': 'https://www.rhein-galerie.de',
        'maps_url': 'https://maps.google.com/?q=Rhein-Galerie+Ludwigshafen',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Rathaus-Center Ludwigshafen',
        'adres': 'Rathausplatz 20, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Şehir merkezinde Belediye binasıyla bütünleşik alışveriş merkezi. Süpermarket, tekstil, çeşitli hizmet mağazaları ve kafeterya ile şehir merkezinin ulaşılabilir alışveriş noktasıdır.',
        'website': 'https://www.rathauscenter-ludwigshafen.de',
        'maps_url': 'https://maps.google.com/?q=Rathaus-Center+Ludwigshafen+Rathausplatz',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Ludwigshafen Innenstadt — Einkaufsmeile',
        'adres': 'Bismarckstraße / Ludwigsstraße, 67059 Ludwigshafen am Rhein',
        'aciklama': 'Ludwigshafen\'ın ana alışveriş caddesi. Zara, H&M, C&A, Kaufhof ve çok sayıda yerel mağazanın yer aldığı bu aksda tüm temel ihtiyaçlar karşılanabilmektedir.',
        'website': 'https://www.ludwigshafen.de/wirtschaft/wirtschaftsstandort/innenstadt/',
        'maps_url': 'https://maps.google.com/?q=Bismarckstraße+Ludwigshafen+Einkaufsstraße',
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
        ludwigshafen = Stadt.objects.get(slug='ludwigshafen')
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
                stadt=ludwigshafen,
                defaults={
                    'eyalet': eyalet,
                    'scope': 'stadt',
                    'tur': 'yer',
                    'kategori': kategori_slug,
                    'adres': veri['adres'],
                    'sehir': 'Ludwigshafen am Rhein',
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
    Yer.objects.filter(ad__in=adlar, sehir='Ludwigshafen am Rhein').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0026_yerkategori_ibadet_tuv_alisveris'),
        ('stadt', '0024_ludwigshafen_aktiv'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
