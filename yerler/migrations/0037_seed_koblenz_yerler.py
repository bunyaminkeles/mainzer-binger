from django.db import migrations

RESMI_KURUM = [
    {'ad': 'Rathaus Koblenz', 'adres': 'Josef-Görres-Platz 1, 56068 Koblenz', 'aciklama': 'Koblenz şehir belediyesi. Belediye başkanlığı, nüfus müdürlüğü ve diğer şehir hizmetleri burada yer alır.', 'website': 'https://www.koblenz.de/rathaus/', 'maps_url': 'https://maps.google.com/?q=Rathaus+Koblenz,+Josef-Görres-Platz+1,+56068+Koblenz'},
    {'ad': 'Ausländerbehörde Koblenz', 'adres': 'Ludwig-Erhard-Str. 2, 56073 Koblenz', 'aciklama': 'Oturma izni, vize uzatma ve yabancılara yönelik tüm resmi işlemlerin yapıldığı birim. Randevu zorunludur.', 'website': 'https://www.koblenz.de/buergerservice/abteilungen/RLP:department:345950/auslaenderangelegenheiten/', 'maps_url': 'https://maps.google.com/?q=Ausländerbehörde+Koblenz,+Ludwig-Erhard-Str.+2,+56073+Koblenz'},
    {'ad': 'Bürgeramt Koblenz', 'adres': 'Gymnasialstr. 4-8, 56068 Koblenz', 'aciklama': 'Nüfus tescil, kimlik ve pasaport işlemleri, adres değişikliği ve diğer vatandaş hizmetlerini sunar.', 'website': 'https://www.koblenz.de/rathaus/verwaltung/aemter-und-abteilungen-a-z/buergeramt-der-stadt-koblenz/', 'maps_url': 'https://maps.google.com/?q=Bürgeramt+Koblenz,+Gymnasialstraße+4,+56068+Koblenz'},
    {'ad': 'Finanzamt Koblenz', 'adres': 'Ferdinand-Sauerbruch-Str. 19, 56073 Koblenz', 'aciklama': 'Gelir vergisi beyanı, vergi numarası alma ve tüm vergi işlemlerinin yapıldığı resmi devlet kurumu.', 'website': 'https://fa-koblenz.rlp.de/', 'maps_url': 'https://maps.google.com/?q=Finanzamt+Koblenz,+Ferdinand-Sauerbruch-Str.+19,+56073+Koblenz'},
    {'ad': 'Jobcenter Koblenz', 'adres': 'Carl-Löhr-Str. 6, 56070 Koblenz', 'aciklama': 'İş bulma desteği, Bürgergeld başvurusu ve sosyal yardım hizmetleri sunan iş ve sosyal güvenlik merkezi.', 'website': 'https://jobcenter-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Jobcenter+Koblenz,+Carl-Löhr-Str.+6,+56070+Koblenz'},
]

IBADET = [
    {'ad': 'DITIB Türkisch-Islamische Gemeinde Koblenz', 'adres': 'Theo-Mackeben-Str. 2, 56070 Koblenz', 'aciklama': 'Koblenz\'teki ana DITIB Türk-İslam cemaati camii. Türkçe Cuma hutbesi ve Kuran kursları düzenlenmektedir.', 'website': 'https://www.ditib.de/', 'maps_url': 'https://maps.google.com/?q=DITIB+Koblenz,+Theo-Mackeben-Str.+2,+56070+Koblenz'},
    {'ad': 'Tahir-Moschee Koblenz', 'adres': 'Am Franzosenfriedhof 3-7, 56070 Koblenz', 'aciklama': 'Ahmadiyya Müslüman Cemaati\'ne ait cami. 500 kişilik kapasiteye sahip, Koblenz-Lützel semtindedir.', 'website': 'https://ahmadiyya.de/gebetsstaette/moscheen/koblenz/', 'maps_url': 'https://maps.google.com/?q=Tahir+Moschee+Koblenz,+Am+Franzosenfriedhof,+56070+Koblenz'},
    {'ad': 'Al-Aqsa-Moschee Koblenz', 'adres': 'Mayer-Alberti-Straße 8, 56070 Koblenz', 'aciklama': 'İslam Kültür Merkezi bünyesindeki cami.', 'website': 'https://www.aqsamoschee-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Al-Aqsa+Moschee+Koblenz,+Mayer-Alberti-Straße+8,+56070+Koblenz'},
    {'ad': 'Liebfrauenkirche Koblenz', 'adres': 'Florinspfaffengasse 14, 56068 Koblenz', 'aciklama': 'Koblenz eski şehir merkezindeki önemli Katolik kilisesi. Yaklaşık 1200 yılında inşa edilmiş tarihi Romanesque yapı.', 'website': 'http://www.liebfrauen-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Liebfrauenkirche+Koblenz,+56068+Koblenz'},
    {'ad': 'Florinskirche Koblenz', 'adres': 'Florinsmarkt, 56068 Koblenz', 'aciklama': '1100\'lü yıllara dayanan Romanesque tarzı Protestan kilisesi. Koblenz\'in eski şehir siluetine hakim tarihi yapı.', 'website': 'https://koblenz-mitte.ekir.de/', 'maps_url': 'https://maps.google.com/?q=Florinskirche+Koblenz,+Florinsmarkt,+56068+Koblenz'},
]

TUV = [
    {'ad': 'TÜV Rheinland Prüfstelle Koblenz', 'adres': 'Hans-Böckler-Straße 6, 56070 Koblenz', 'aciklama': 'TÜV Rheinland araç muayene istasyonu. Hauptuntersuchung (HU) ve egzoz gazı muayenesi yapılmaktadır.', 'website': 'https://www.tuv.com/germany/de/', 'maps_url': 'https://maps.google.com/?q=TÜV+Rheinland+Koblenz,+Hans-Böckler-Straße+6,+56070+Koblenz'},
    {'ad': 'DEKRA Niederlassung Koblenz', 'adres': 'Wallersheimer Weg 63-67, 56070 Koblenz', 'aciklama': 'DEKRA araç muayene merkezi. HU, AU (egzoz muayenesi) ve sürücü belgesi sınavları düzenlenmektedir.', 'website': 'https://www.dekra.de/de/koblenz/', 'maps_url': 'https://maps.google.com/?q=DEKRA+Koblenz,+Wallersheimer+Weg+63,+56070+Koblenz'},
]

SAGLIK = [
    {'ad': 'Gemeinschaftsklinikum Mittelrhein – Kemperhof', 'adres': 'Koblenzer Str. 115-155, 56073 Koblenz', 'aciklama': 'Koblenz\'in en büyük hastanelerinden biri. Çok sayıda uzmanlık bölümüyle tam teşekküllü genel hastane.', 'website': 'https://www.gk.de/', 'maps_url': 'https://maps.google.com/?q=Kemperhof+Koblenz,+Koblenzer+Straße+115,+56073+Koblenz'},
    {'ad': 'Gemeinschaftsklinikum – Ev. Stift St. Martin', 'adres': 'Johannes-Müller-Str. 7, 56068 Koblenz', 'aciklama': 'Şehir merkezinde yer alan genel hastane. Dahiliye, cerrahi ve çeşitli uzman klinikleri bulunmaktadır.', 'website': 'https://www.gk.de/', 'maps_url': 'https://maps.google.com/?q=Ev.+Stift+St.+Martin+Koblenz,+Johannes-Müller-Straße+7,+56068+Koblenz'},
    {'ad': 'Katholisches Klinikum – Brüderhaus Koblenz', 'adres': 'Kardinal-Krementz-Str. 1-5, 56073 Koblenz', 'aciklama': 'Onkoloji, ortopedi ve diğer branşlarda uzman ekipler görev yapar.', 'website': 'https://www.kk-km.de/', 'maps_url': 'https://maps.google.com/?q=Brüderhaus+Koblenz,+Kardinal-Krementz-Straße+1,+56073+Koblenz'},
    {'ad': 'Katholisches Klinikum – Marienhof Koblenz', 'adres': 'Rudolf-Virchow-Str. 7-9, 56073 Koblenz', 'aciklama': 'Gynekologie, kadın doğum ve çocuk sağlığı alanlarında uzmanlaşmış hastane.', 'website': 'https://www.kk-km.de/', 'maps_url': 'https://maps.google.com/?q=Marienhof+Koblenz,+Rudolf-Virchow-Straße+7,+56073+Koblenz'},
]

EGITIM = [
    {'ad': 'Universität Koblenz', 'adres': 'Universitätsstr. 1, 56070 Koblenz', 'aciklama': 'Koblenz Üniversitesi. Bilgisayar bilimleri, eğitim ve doğa bilimleri bölümleri mevcuttur.', 'website': 'https://www.uni-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Universität+Koblenz,+Universitätsstraße+1,+56070+Koblenz'},
    {'ad': 'Hochschule Koblenz', 'adres': 'Konrad-Zuse-Str. 1, 56075 Koblenz', 'aciklama': 'Uygulamalı bilimler üniversitesi. Mühendislik, işletme ve sosyal bilimler alanlarında eğitim verir.', 'website': 'https://www.hs-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Hochschule+Koblenz,+Konrad-Zuse-Str.+1,+56075+Koblenz'},
    {'ad': 'Volkshochschule (VHS) Koblenz', 'adres': 'Hoevelstr. 6, 56073 Koblenz', 'aciklama': 'Halk eğitim merkezi. Entegrasyon kursları, Almanca dil kursları ve mesleki eğitim düzenler.', 'website': 'https://www.vhs-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=VHS+Koblenz,+Hoevelstraße+6,+56073+Koblenz'},
    {'ad': 'Berlitz Sprachschule Koblenz', 'adres': 'Stegemannstraße 44, 56068 Koblenz', 'aciklama': 'Özel dil okulu. Almanca, İngilizce ve diğer dillerde bireysel ve grup kursları sunar.', 'website': 'https://www.berlitz.com/de-de/sprachschulen/koblenz', 'maps_url': 'https://maps.google.com/?q=Berlitz+Koblenz,+Stegemannstraße+44,+56068+Koblenz'},
]

GEZI = [
    {'ad': 'Deutsches Eck', 'adres': 'Konrad-Adenauer-Ufer, 56068 Koblenz', 'aciklama': 'Ren ve Mosel nehirlerinin birleştiği efsanevi burun. Kaiser Wilhelm anıtı ile Koblenz\'in en simgesel noktasıdır.', 'website': 'https://www.visit-koblenz.de/en/sights/deutsches-eck', 'maps_url': 'https://maps.google.com/?q=Deutsches+Eck+Koblenz,+56068+Koblenz'},
    {'ad': 'Festung Ehrenbreitstein', 'adres': 'Greiffenklaustraße 5, 56077 Koblenz', 'aciklama': 'Avrupa\'nın en büyük ikinci kalesi. Ren\'in 118 metre yukarısında; Landesmuseum ve muhteşem şehir manzarası sunar.', 'website': 'https://tor-zum-welterbe.de/festung-ehrenbreitstein', 'maps_url': 'https://maps.google.com/?q=Festung+Ehrenbreitstein,+56077+Koblenz'},
    {'ad': 'Seilbahn Koblenz (Teleferik)', 'adres': 'Konrad-Adenauer-Ufer, 56068 Koblenz', 'aciklama': 'Ren üzerinden Ehrenbreitstein Kalesi\'ne ulaştıran teleferik. Eşsiz panoramik manzara sunar.', 'website': 'https://www.seilbahn-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Seilbahn+Koblenz,+Konrad-Adenauer-Ufer,+56068+Koblenz'},
    {'ad': 'Basilika St. Kastor', 'adres': 'Kastorhof 8, 56068 Koblenz', 'aciklama': 'Koblenz\'in en eski kilisesi. Deutsches Eck\'in hemen arkasında, nehir kavşağına bakan tarihi yapı.', 'website': 'http://www.sankt-kastor-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Basilika+St.+Kastor+Koblenz,+Kastorhof+8,+56068+Koblenz'},
    {'ad': 'Altstadt Koblenz (Florinsmarkt)', 'adres': 'Florinsmarkt, 56068 Koblenz', 'aciklama': 'Koblenz\'in tarihi Altstadt bölgesi. Florinskirche, tarihi meydanlar ve ortaçağ mimarisiyle yürüyüş cenneti.', 'website': 'https://www.visit-koblenz.de/', 'maps_url': 'https://maps.google.com/?q=Florinsmarkt,+56068+Koblenz'},
]

ALISVERIS = [
    {'ad': 'Forum Mittelrhein', 'adres': 'Zentralplatz 1, 56068 Koblenz', 'aciklama': '2012\'de açılan şehir merkezi AVM. 80\'den fazla mağaza, 24.000 m² kapalı alan.', 'website': 'https://www.forum-mittelrhein.com/', 'maps_url': 'https://maps.google.com/?q=Forum+Mittelrhein,+Zentralplatz+1,+56068+Koblenz'},
    {'ad': 'Löhr-Center Koblenz', 'adres': 'Hohenfelder Str. 22, 56068 Koblenz', 'aciklama': '130 mağaza ve 32.000 m² satış alanına sahip büyük AVM. Giyim, elektronik, restoran ve market seçenekleri mevcuttur.', 'website': 'https://www.loehr-center.de/', 'maps_url': 'https://maps.google.com/?q=Löhr-Center+Koblenz,+Hohenfelder+Straße+22,+56068+Koblenz'},
    {'ad': 'GLOBUS Markthalle Koblenz', 'adres': 'Jakob-Caspers-Str. 2, 56070 Koblenz', 'aciklama': 'Yaklaşık 10.000 m² satış alanına sahip büyük hipermarket. Geniş gıda, elektronik ve ev eşyası yelpazesiyle bilinir.', 'website': 'https://www.globus.de/koblenz/', 'maps_url': 'https://maps.google.com/?q=Globus+Koblenz,+Jakob-Caspers-Straße+2,+56070+Koblenz'},
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        sehir  = Stadt.objects.get(slug='koblenz')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return
    for kategori_slug, veriler in [
        ('resmi_kurum', RESMI_KURUM), ('ibadet', IBADET), ('tuv', TUV),
        ('saglik', SAGLIK), ('egitim', EGITIM), ('gezi', GEZI), ('alisveris', ALISVERIS),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet': eyalet, 'scope': 'stadt', 'tur': 'yer',
                    'kategori': kategori_slug, 'sehir': 'Koblenz',
                    'adres': veri['adres'], 'aciklama': veri['aciklama'],
                    'kapak_resmi': '', 'website': veri.get('website', ''),
                    'maps_url': veri.get('maps_url', ''), 'icerik': '',
                    'aktif': True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Koblenz').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0036_seed_westerburg_yerler'),
        ('stadt',  '0020_koblenz_aktiv'),
    ]

    operations = [migrations.RunPython(seed, unseed)]
