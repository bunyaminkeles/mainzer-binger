from django.db import migrations

RESMI_KURUM = [
    {
        'ad': 'Amt für Ausländerfragen Trier',
        'adres': 'Beutelstr. 67, 54290 Trier',
        'aciklama': "Trier Yabancılar Dairesi. Oturma izni, çalışma izni, aile birleşimi ve seyahat belgesi işlemleri yapılmaktadır. Ziyaret için önceden randevu alınması zorunludur.",
        'website': 'https://www.trier.de/rathaus-buerger-in/stadtverwaltung/aemter-dienststellen/dezernat-ii/amt-fuer-auslaenderfragen/',
        'maps_url': 'https://maps.google.com/?q=Amt+für+Ausländerfragen+Trier+Beutelstr+67+54290',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Jobcenter Trier',
        'adres': 'Dasbachstr. 9, 54292 Trier',
        'aciklama': 'Trier Jobcenter. Bürgergeld (Sosyal Yardım) başvurusu, iş arama desteği, entegrasyon danışmanlığı ve mesleki yeniden yönlendirme hizmetleri sunulmaktadır.',
        'website': 'https://www.jobcenter-trier.de',
        'maps_url': 'https://maps.google.com/?q=Jobcenter+Trier+Dasbachstr+9+54292',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Bürgerservice Stadt Trier — Terminvereinbarung',
        'adres': 'Am Augustinerhof, 54290 Trier',
        'aciklama': "Trier Belediyesi Vatandaş Hizmetleri. Pasaport, kimlik, araç tescil ve ikamet kaydı gibi idari işlemler için merkezi hizmet noktası. Online randevu: trier.de/terminvereinbarung.",
        'website': 'https://www.trier.de/rathaus-buerger-in/buergerservice/terminvereinbarung/',
        'maps_url': 'https://maps.google.com/?q=Rathaus+Trier+Am+Augustinerhof+54290',
        'kapak_resmi': '', 'icerik': '',
    },
]

IBADET = [
    {
        'ad': 'DITIB Türkisch-Islamische Gemeinde Trier',
        'adres': 'Gartenstr. 33, 54290 Trier',
        'aciklama': "DITIB bünyesindeki Trier Türk-İslam Derneği Camii. Beş vakit namaz, Kuran kursları, cenaze hizmetleri ve sosyal etkinlikler düzenlenmektedir.",
        'website': 'https://www.ditib.de',
        'maps_url': 'https://maps.google.com/?q=DITIB+Türkisch-Islamische+Gemeinde+Trier+Gartenstr+33',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'IGMG Islamische Gemeinschaft Trier',
        'adres': 'Maarstr. 1, 54292 Trier',
        'aciklama': 'İslam Toplumu Millî Görüş (IGMG) bünyesindeki Trier cemaati. Cuma namazı, Kuran eğitimi ve gençlik programları sunulmaktadır.',
        'website': 'https://www.igmg.org',
        'maps_url': 'https://maps.google.com/?q=IGMG+Islamische+Gemeinschaft+Trier+Maarstr',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Islamisches Kulturzentrum Trier',
        'adres': 'Paulinstr. 18, 54292 Trier',
        'aciklama': "Trier'deki İslam Kültür Merkezi. Beş vakit namaz ve dini-sosyal etkinlikler düzenlenmektedir.",
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Islamisches+Kulturzentrum+Trier+Paulinstr+18',
        'kapak_resmi': '', 'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV Rheinland Kfz-Prüfstelle Trier',
        'adres': 'Metternichstr. 6, 54295 Trier',
        'aciklama': "TÜV Rheinland'ın Trier araç muayene merkezi. HU (Hauptuntersuchung) ve AU (Abgasuntersuchung) başta olmak üzere teknik kontroller yapılmaktadır. Online randevu alınabilir.",
        'website': 'https://www.tuv.com',
        'maps_url': 'https://maps.google.com/?q=TÜV+Rheinland+Trier+Metternichstr+6+54295',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'DEKRA Automobil Station Trier',
        'adres': 'Luxemburger Str. 119, 54294 Trier',
        'aciklama': "DEKRA'nın Trier araç muayene merkezi. HU, AU ve araç değerleme hizmetleri ile teknik ekspertiz sunulmaktadır.",
        'website': 'https://www.dekra.de',
        'maps_url': 'https://maps.google.com/?q=DEKRA+Automobil+Station+Trier+Luxemburger+Str+119',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'GTÜ Kfz-Prüfstelle Trier',
        'adres': 'Eurener Str. 151, 54294 Trier',
        'aciklama': 'GTÜ muayene istasyonu. TÜV ve DEKRA alternatifi, uygun fiyatlı araç periyodik muayenesi (HU/AU).',
        'website': 'https://www.gtue.de',
        'maps_url': 'https://maps.google.com/?q=GTÜ+Kfz-Prüfstelle+Trier+Eurener+Str+151',
        'kapak_resmi': '', 'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'Krankenhaus der Barmherzigen Brüder Trier',
        'adres': 'Nordallee 1, 54292 Trier',
        'aciklama': "Trier'in en büyük hastanesi. 700'den fazla yatak kapasitesiyle kardiyoloji, nöroloji, cerrahi ve birçok uzmanlık dalında 24 saat hizmet vermektedir.",
        'website': 'https://www.bk-trier.de',
        'maps_url': 'https://maps.google.com/?q=Krankenhaus+Barmherzige+Brüder+Trier+Nordallee+1',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Mutterhaus der Borromäerinnen Trier',
        'adres': 'Feldstr. 16, 54290 Trier',
        'aciklama': "Trier'in köklü eğitim ve sağlık merkezi hastanesi. Dahiliye, ortopedi ve rehabilitasyon hizmetleri sunulmaktadır.",
        'website': 'https://www.mutterhaus.de',
        'maps_url': 'https://maps.google.com/?q=Mutterhaus+der+Borromäerinnen+Trier+Feldstr+16',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Gesundheitsamt Trier — Kreis Trier-Saarburg',
        'adres': 'Willy-Brandt-Platz 1, 54290 Trier',
        'aciklama': 'Trier-Saarburg İlçe Sağlık Dairesi. Aşılama, bulaşıcı hastalık bildirimi ve göçmen sağlık danışmanlığı hizmetleri sunulmaktadır.',
        'website': 'https://www.trier-saarburg.de',
        'maps_url': 'https://maps.google.com/?q=Gesundheitsamt+Trier+Willy-Brandt-Platz+1',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Ärztlicher Bereitschaftsdienst — 116 117 (Trier)',
        'adres': 'Nordallee 1, 54292 Trier',
        'aciklama': "KV RLP'nin acil nöbet hattı. Hafta sonu ve gece saatlerinde acil olmayan sağlık sorunları için 116 117 numarasını arayın.",
        'website': 'https://www.kv-rlp.de/patienten/patientenservice-116117',
        'maps_url': '',
        'kapak_resmi': '', 'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'vhs Trier — Volkshochschule',
        'adres': 'Hindenburgstr. 1, 54295 Trier',
        'aciklama': "Trier Halk Eğitim Merkezi. Almanca dil kursları (A1–C2), BAMF entegrasyon kursları, mesleki eğitim ve kültürel programlar.",
        'website': 'https://www.vhs-trier.de',
        'maps_url': 'https://maps.google.com/?q=vhs+Trier+Volkshochschule+Hindenburgstr+1',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Universität Trier',
        'adres': 'Universitätsring 15, 54296 Trier',
        'aciklama': "Trier Üniversitesi. Hukuk, iktisat, sosyal bilimler, dil bilimleri ve psikoloji alanlarında 12.000'den fazla öğrenciye yönelik lisans ve yüksek lisans programları.",
        'website': 'https://www.uni-trier.de',
        'maps_url': 'https://maps.google.com/?q=Universität+Trier+Universitätsring+15+54296',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Hochschule Trier — University of Applied Sciences',
        'adres': 'Schneidershof, 54293 Trier',
        'aciklama': "Trier Uygulamalı Bilimler Üniversitesi. Mühendislik, tasarım, çevre bilimleri ve işletme alanlarında 7.000'den fazla öğrenciye yönelik programlar.",
        'website': 'https://www.hochschule-trier.de',
        'maps_url': 'https://maps.google.com/?q=Hochschule+Trier+Schneidershof+54293',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'BAMF-NAvI — Integrationskurs Trier',
        'adres': 'Telefonla erişim / Online',
        'aciklama': "BAMF entegrasyon kursu rehberi. Trier ve çevresindeki yetkili kurs merkezlerini ve başvuru adımlarını açıklar.",
        'website': 'https://bamf-navi.bamf.de',
        'maps_url': '',
        'kapak_resmi': '', 'icerik': '',
    },
]

GEZI = [
    {
        'ad': 'Porta Nigra Trier',
        'adres': 'Porta-Nigra-Platz, 54290 Trier',
        'aciklama': "UNESCO Dünya Mirası. MS 180 yılına tarihlenen Roma döneminin en iyi korunmuş kapı yapısı. Trier'in simgesi ve Almanya'nın en büyük Roma eseri.",
        'website': 'https://www.trier-info.de/sehenswuerdigkeiten/porta-nigra',
        'maps_url': 'https://maps.google.com/?q=Porta+Nigra+Trier+Porta-Nigra-Platz',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Amphitheater Trier',
        'adres': 'Olewiger Str. 25, 54295 Trier',
        'aciklama': "MS 100 yılına tarihlenen Roma amfitiyatrosu. 20.000 seyirci kapasitesiyle UNESCO Dünya Mirası listesindedir. Yaz aylarında çeşitli etkinliklere ev sahipliği yapar.",
        'website': 'https://www.trier-info.de/sehenswuerdigkeiten/amphitheater',
        'maps_url': 'https://maps.google.com/?q=Amphitheater+Trier+Olewiger+Str+25',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Konstantinbasilika (Aula Palatina) Trier',
        'adres': 'Konstantinplatz 10, 54290 Trier',
        'aciklama': "Günümüze ulaşmış en büyük Roma saray salonu. İmparator Konstantin tarafından MS 310 yılında inşa edilmiş olup bugün Protestan kilisesi olarak kullanılmaktadır.",
        'website': 'https://www.evangelisch-trier.de/gemeinden/konstantinbasilika',
        'maps_url': 'https://maps.google.com/?q=Konstantinbasilika+Trier+Konstantinplatz+10',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Rheinisches Landesmuseum Trier',
        'adres': 'Weimarer Allee 1, 54290 Trier',
        'aciklama': "Almanya'nın en önemli Roma arkeoloji müzelerinden biri. Roma dönemi buluntuları, heykeller ve Trier'in antik tarihine ilişkin kapsamlı koleksiyonlar sergilenmektedir.",
        'website': 'https://www.landesmuseum-trier.de',
        'maps_url': 'https://maps.google.com/?q=Rheinisches+Landesmuseum+Trier+Weimarer+Allee+1',
        'kapak_resmi': '', 'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'Römerpassage Trier',
        'adres': 'Fleischstr. 61, 54290 Trier',
        'aciklama': "Trier şehir merkezindeki modern alışveriş pasajı. Moda, aksesuar ve hizmet mağazalarıyla şehir merkezinin en işlek alışveriş noktalarından biri.",
        'website': 'https://www.roemerpassage.de',
        'maps_url': 'https://maps.google.com/?q=Römerpassage+Trier+Fleischstr+61',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'GALERIA Trier',
        'adres': 'Simeonstr. 52-54, 54290 Trier',
        'aciklama': 'Porta Nigra yakınındaki GALERIA alışveriş mağazası. Giyim, kozmetik ve ev ürünleri bölümleriyle kapsamlı alışveriş imkânı.',
        'website': 'https://www.galeria.de',
        'maps_url': 'https://maps.google.com/?q=GALERIA+Trier+Simeonstr+52+54290',
        'kapak_resmi': '', 'icerik': '',
    },
    {
        'ad': 'Trier Innenstadt — Einkaufsmeile',
        'adres': 'Simeonstraße / Fleischstraße, 54290 Trier',
        'aciklama': "Trier'in ana yürüyüş ve alışveriş aksı. H&M, Zara, C&A ve çok sayıda yerel mağazanın yer aldığı tarihi şehir merkezinde tüm temel ihtiyaçlar karşılanabilir.",
        'website': 'https://www.trier-info.de/einkaufen',
        'maps_url': 'https://maps.google.com/?q=Simeonstraße+Trier+Einkaufsstraße',
        'kapak_resmi': '', 'icerik': '',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        trier = Stadt.objects.get(slug='trier')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    kategoriler = [
        ('resmi_kurum', RESMI_KURUM),
        ('ibadet',      IBADET),
        ('tuv',         TUV),
        ('saglik',      SAGLIK),
        ('egitim',      EGITIM),
        ('gezi',        GEZI),
        ('alisveris',   ALISVERIS),
    ]

    for kategori_slug, veriler in kategoriler:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'],
                stadt=trier,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'adres':       veri['adres'],
                    'sehir':       'Trier',
                    'aciklama':    veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''),
                    'website':     veri.get('website', ''),
                    'maps_url':    veri.get('maps_url', ''),
                    'icerik':      veri.get('icerik', ''),
                    'aktif':       True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = (
        [v['ad'] for v in RESMI_KURUM] + [v['ad'] for v in IBADET] +
        [v['ad'] for v in TUV] + [v['ad'] for v in SAGLIK] +
        [v['ad'] for v in EGITIM] + [v['ad'] for v in GEZI] +
        [v['ad'] for v in ALISVERIS]
    )
    Yer.objects.filter(ad__in=adlar, sehir='Trier').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0028_fix_rlp_worms_ludwigshafen_yerler'),
        ('stadt', '0026_trier_aktiv'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
