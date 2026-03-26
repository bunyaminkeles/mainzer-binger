from django.db import migrations


BASKENTLER = [
    {
        'eyalet_kod': 'BW',
        'name': 'Stuttgart',
        'slug': 'stuttgart',
        'lat': 48.777500,
        'lng': 9.180000,
        'population': 612663,
        'beschreibung': (
            'Stuttgart, Baden-Württemberg\'in başkenti ve Almanya\'nın altıncı en büyük şehridir. '
            '"Otomobilin beşiği" olarak bilinir ve Mercedes-Benz ile Porsche gibi dünyaca ünlü '
            'otomotiv şirketlerine ev sahipliği yapar. Yüksek teknoloji endüstrisi ve güçlü '
            'ekonomisiyle Avrupa\'nın önde gelen metropolitan alanlarından biridir.'
        ),
    },
    {
        'eyalet_kod': 'BY',
        'name': 'München',
        'slug': 'muenchen',
        'lat': 48.137500,
        'lng': 11.575000,
        'population': 1505005,
        'beschreibung': (
            'Bavyera\'nın başkenti olan Münih, Almanya\'nın üçüncü büyük şehridir ve yaklaşık '
            '1,5 milyon nüfusa sahiptir. Isar Nehri üzerinde Alpler\'in kuzeyinde yer alan şehir, '
            'yüksek teknoloji, otomotiv ve finans sektörlerinin merkezidir. Münih, mimarlığı, '
            'kültürel mekanları ve dünya çapındaki Oktoberfest etkinliğiyle tanınmaktadır.'
        ),
    },
    {
        'eyalet_kod': 'BE',
        'name': 'Berlin',
        'slug': 'berlin',
        'lat': 52.520000,
        'lng': 13.405000,
        'population': 3685265,
        'beschreibung': (
            'Almanya\'nın başkenti ve en büyük şehri olan Berlin, Avrupa Birliği\'nin en kalabalık '
            'şehirlerinden biridir. Zengin tarihi mirası, sanat ve kültür merkezleri ile modern '
            'mimarlığıyla ünlüdür. 1990 yılında yeniden birleşerek günümüzde yüksek teknoloji, '
            'hizmet sektörü ve yaratıcı endüstrilerin merkezi haline gelmiştir.'
        ),
    },
    {
        'eyalet_kod': 'BB',
        'name': 'Potsdam',
        'slug': 'potsdam',
        'lat': 52.400560,
        'lng': 13.059170,
        'population': 184754,
        'beschreibung': (
            'Potsdam, Brandenburg eyaletinin başkenti olup Havel Nehri üzerinde yer almaktadır. '
            'UNESCO Dünya Mirası listesindeki Sanssouci Sarayı ve parkları ile ünlüdür. '
            '1945 yılında yapılan Potsdam Konferansı\'na ev sahipliği yapmasıyla tarihsel önem taşımaktadır.'
        ),
    },
    {
        'eyalet_kod': 'HB',
        'name': 'Bremen',
        'slug': 'bremen',
        'lat': 53.075830,
        'lng': 8.807220,
        'population': 586271,
        'beschreibung': (
            'Bremen, Almanya\'nın kuzeybatısında yer alan önemli bir liman kentidir. '
            'Weser Nehri üzerinde konumlanmış olan şehir, Hansa Birliği\'nin tarihi bir üyesidir '
            've ülkenin ikinci büyük limanına ev sahipliği yapmaktadır. '
            'Tarihi şehir merkezi ve Bremen Mızıkacıları heykeli ile tanınmaktadır.'
        ),
    },
    {
        'eyalet_kod': 'HH',
        'name': 'Hamburg',
        'slug': 'hamburg',
        'lat': 53.550000,
        'lng': 10.000000,
        'population': 1973896,
        'beschreibung': (
            'Almanya\'nın ikinci büyük şehri Hamburg, Elbe Nehri\'nin Kuzey Deniz\'e açılan ağzında '
            'konumlanmış önemli bir liman kentidir. Avrupa\'nın üçüncü büyük limanına sahip olan '
            'şehir, tarihi Hansa Birliği üyeliğiyle köklü bir ticari geçmişe sahiptir. '
            'Reeperbahn eğlence bölgesi ve Elbphilharmonie konser salonu ile ünlüdür.'
        ),
    },
    {
        'eyalet_kod': 'HE',
        'name': 'Wiesbaden',
        'slug': 'wiesbaden',
        'lat': 50.082500,
        'lng': 8.240000,
        'population': 288850,
        'beschreibung': (
            'Wiesbaden, Hessen eyaletinin başkenti olup Almanya\'nın köklü kaplıca kentlerinden biridir. '
            'Rhine Nehri\'nin sağ kıyısında yer alan şehir, 15 mineral su kaynağıyla "Kuzey\'in Nizza\'sı" '
            'olarak anılmaktadır. Şaşaalı Wilhelmstraße caddesi ve tarihi kaplıcalarıyla tanınmaktadır.'
        ),
    },
    {
        'eyalet_kod': 'MV',
        'name': 'Schwerin',
        'slug': 'schwerin',
        'lat': 53.633000,
        'lng': 11.417000,
        'population': 98308,
        'beschreibung': (
            'Schwerin, Mecklenburg-Vorpommern eyaletinin başkenti olup Schweriner Gölü\'nün kıyısında '
            'yer almaktadır. Romantik Schwerin Sarayı\'nın altın kubbeleriyle ünlü olan şehir, '
            'çok sayıda göl ve yeşil alanıyla "Göller Şehri" olarak da bilinmektedir. '
            'Tarihi Altstadt ve Schelfstadt mahalleleri korunmuş yapı dokusuyla dikkat çekmektedir.'
        ),
    },
    {
        'eyalet_kod': 'NI',
        'name': 'Hannover',
        'slug': 'hannover',
        'lat': 52.367000,
        'lng': 9.717000,
        'population': 522131,
        'beschreibung': (
            'Hannover, Aşağı Saksonya\'nın başkenti ve Almanya\'nın önemli ticaret merkezlerinden biridir. '
            'Dünyanın en büyük sanayi fuarı olan Hannover Messe\'ye ev sahipliği yapmaktadır. '
            'Leine Nehri kıyısında kurulu olan şehir, önemli bir ulaşım ve lojistik merkezidir.'
        ),
    },
    {
        'eyalet_kod': 'NW',
        'name': 'Düsseldorf',
        'slug': 'duesseldorf',
        'lat': 51.225600,
        'lng': 6.776700,
        'population': 618685,
        'beschreibung': (
            'Düsseldorf, Kuzey Ren-Vestfalya eyaletinin başkenti ve Almanya\'nın uluslararası iş merkezlerinden biridir. '
            'Düssel Nehri\'nin Rhine\'a döküldüğü yerde kurulmuş olan şehir, moda, sanat ve ticaret alanlarında '
            'öne çıkmaktadır. Königsallee (Kö) alışveriş caddesi ve canlı Altstadt mahallesiyle tanınmaktadır.'
        ),
    },
    {
        'eyalet_kod': 'SL',
        'name': 'Saarbrücken',
        'slug': 'saarbruecken',
        'lat': 49.233000,
        'lng': 7.000000,
        'population': 182971,
        'beschreibung': (
            'Saarbrücken, Saarland eyaletinin başkenti ve Fransa sınırına yakın konumuyla önemli '
            'bir sınır kentidir. Saar Nehri kıyısında kurulu olan şehir, köklü endüstriyel geçmişi '
            've Fransız kültürel etkisiyle kendine özgü bir karakter taşımaktadır. '
            'Schlossplatz meydanı ve baroko saray yapısı şehrin simgeleri arasındadır.'
        ),
    },
    {
        'eyalet_kod': 'SN',
        'name': 'Dresden',
        'slug': 'dresden',
        'lat': 51.050000,
        'lng': 13.740000,
        'population': 564904,
        'beschreibung': (
            'Dresden, Saksonya eyaletinin başkenti olup "Elbe\'nin Floransa\'sı" olarak anılmaktadır. '
            'Barok ve Rokoko mimarisiyle ünlü olan şehir, Zwinger Sarayı ve Frauenkirche gibi '
            'tarihi yapılara ev sahipliği yapmaktadır. İkinci Dünya Savaşı\'nda ağır hasar görmüş '
            'ancak yeniden inşa edilerek Almanya\'nın önemli kültür merkezlerinden biri olmuştur.'
        ),
    },
    {
        'eyalet_kod': 'ST',
        'name': 'Magdeburg',
        'slug': 'magdeburg',
        'lat': 52.131670,
        'lng': 11.639170,
        'population': 244329,
        'beschreibung': (
            'Magdeburg, Saksonya-Anhalt eyaletinin başkenti olup Elbe Nehri kıyısında yer almaktadır. '
            'Almanya\'nın en eski şehirlerinden biri olan Magdeburg, İmparator Otto I tarafından '
            'kurulmuş ve Orta Çağ\'da önemli bir ticaret merkezi olmuştur. '
            'Dom katedrali ve modern mimarinin bir arada bulunduğu dinamik bir şehirdir.'
        ),
    },
    {
        'eyalet_kod': 'SH',
        'name': 'Kiel',
        'slug': 'kiel',
        'lat': 54.320000,
        'lng': 10.140000,
        'population': 252668,
        'beschreibung': (
            'Kiel, Schleswig-Holstein eyaletinin başkenti ve Baltık Denizi kıyısındaki önemli bir '
            'liman kentidir. Dünyanın en yoğun kullanılan yapay su yolu olan Kiel Kanalı\'nın '
            'terminusuna ev sahipliği yapmaktadır. Uluslararası yelkencilik yarışması Kieler Woche '
            've gemi inşaat sanayi şehrin öne çıkan özellikleridir.'
        ),
    },
    {
        'eyalet_kod': 'TH',
        'name': 'Erfurt',
        'slug': 'erfurt',
        'lat': 50.978060,
        'lng': 11.028890,
        'population': 218793,
        'beschreibung': (
            'Erfurt, Thüringen eyaletinin başkenti ve en büyük şehridir. '
            '742 yılından itibaren tarihi kaynaklarda geçen şehir, Orta Avrupa\'nın en iyi korunmuş '
            'ortaçağ şehir merkezlerinden birine sahiptir. Krämerbrücke köprüsü ve Erfurt Katedrali '
            'şehrin tarihi dokusunun simgeleridir.'
        ),
    },
]


def seed_baskentler(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')

    for veri in BASKENTLER:
        try:
            eyalet = Eyalet.objects.get(kod=veri['eyalet_kod'])
        except Eyalet.DoesNotExist:
            continue

        Stadt.objects.get_or_create(
            slug=veri['slug'],
            defaults={
                'eyalet': eyalet,
                'name': veri['name'],
                'typ': 'kreisfrei',
                'lat': veri['lat'],
                'lng': veri['lng'],
                'population': veri['population'],
                'beschreibung': veri['beschreibung'],
                'aktiv': True,
            }
        )


def unseed_baskentler(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    slugs = [v['slug'] for v in BASKENTLER]
    Stadt.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0009_seed_icerik_eyalet'),
    ]

    operations = [
        migrations.RunPython(seed_baskentler, unseed_baskentler),
    ]
