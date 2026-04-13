from django.db import migrations

GEZI = [
    {
        'ad': 'Mainzer Dom (Hoher Dom St. Martin)',
        'adres': 'Domstraße 3, 55116 Mainz',
        'aciklama': 'Mainz\'ın simgesi, 1000 yıllık Romanesk katedrali. Mainz Başpiskoposluğu\'nun merkezi ve UNESCO mirası.',
        'website': 'https://www.bistum-mainz.de/dom/',
        'maps_url': 'https://www.google.com/maps/search/Mainzer+Dom+Domstrasse+3+Mainz',
    },
    {
        'ad': 'Gutenberg-Museum',
        'adres': 'Liebfrauenplatz 5, 55116 Mainz',
        'aciklama': 'Matbaacılığın mucidi Johannes Gutenberg\'e adanmış dünya müzesi. Orijinal Gutenberg İncili sergilenmektedir.',
        'website': 'https://www.gutenberg-museum.de/',
        'maps_url': 'https://www.google.com/maps/search/Gutenberg+Museum+Liebfrauenplatz+5+Mainz',
    },
    {
        'ad': 'Kurfürstliches Schloss Mainz',
        'adres': 'Rheinstraße 44, 55116 Mainz',
        'aciklama': 'Rönesans döneminden kalma Seçici Prensler Sarayı. Ren Nehri kıyısında ihtişamlı tarihi yapı.',
        'website': 'https://www.mainz.de/sehenswuerdigkeiten/kurfuerstliches-schloss.php',
        'maps_url': 'https://www.google.com/maps/search/Kurfürstliches+Schloss+Mainz+Rheinstrasse',
    },
    {
        'ad': 'Rheinpromenade Mainz',
        'adres': 'Rheinufer, 55116 Mainz',
        'aciklama': 'Ren Nehri boyunca uzanan tarihi yürüyüş promenadı. Wiesbaden\'e bakan panoramik manzarası ve kafelerle canlı bir buluşma noktası.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Rheinpromenade+Mainz',
    },
    {
        'ad': 'Stephanskirche (Chagall Pencereleri)',
        'adres': 'Kleine Weißgasse 12, 55116 Mainz',
        'aciklama': 'Marc Chagall\'ın tasarladığı mavi vitray pencereleriyle ünlü Gotik kilise. Yahudi-Hristiyan uzlaşısının simgesi.',
        'website': 'https://www.st-stephan-mainz.de/',
        'maps_url': 'https://www.google.com/maps/search/Stephanskirche+Mainz+Kleine+Weißgasse',
    },
    {
        'ad': 'Drususstein (Roma Anıtı)',
        'adres': 'Zitadelle, 55116 Mainz',
        'aciklama': 'M.Ö. 13\'te şehri kuran Romalı general Drusus\'a ait anıt mezar kalıntısı. Mainz\'ın en eski yapısı.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Drususstein+Zitadelle+Mainz',
    },
    {
        'ad': 'Mainz Zitadelle',
        'adres': 'Obentrautstraße, 55118 Mainz',
        'aciklama': '17. yüzyıldan kalma tarihi kale. Günümüzde kültür etkinlikleri ve açık hava konserleri için kullanılmaktadır.',
        'website': 'https://www.zitadelle-mainz.de/',
        'maps_url': 'https://www.google.com/maps/search/Zitadelle+Mainz+Obentrautstrasse',
    },
    {
        'ad': 'Landesmuseum Mainz',
        'adres': 'Große Bleiche 49-51, 55116 Mainz',
        'aciklama': 'Eyalet müzesi. Roma döneminden günümüze Rheinland-Pfalz tarihini, arkeolojisini ve sanatını sergiler.',
        'website': 'https://www.landesmuseum-mainz.de/',
        'maps_url': 'https://www.google.com/maps/search/Landesmuseum+Mainz+Große+Bleiche',
    },
    {
        'ad': 'Mainzer Altstadt',
        'adres': 'Augustinerstraße / Kirschgarten, 55116 Mainz',
        'aciklama': 'Savaş sonrası restore edilen tarihi eski şehir merkezi. Yarı ahşap evler, dar sokaklar ve şarap barlarıyla gezmesi keyifli bölge.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Mainzer+Altstadt+Augustinerstrasse',
    },
    {
        'ad': 'Staatstheater Mainz',
        'adres': 'Gutenbergplatz 7, 55116 Mainz',
        'aciklama': 'Mainz\'ın ana opera ve tiyatro binası. Opera, bale ve dram gösterileri sunar.',
        'website': 'https://www.staatstheater-mainz.com/',
        'maps_url': 'https://www.google.com/maps/search/Staatstheater+Mainz+Gutenbergplatz',
    },
    {
        'ad': 'Mainz Fastnacht Müzesi (Fastnachtsmuseum)',
        'adres': 'Eisgrubweg 1, 55116 Mainz',
        'aciklama': 'Almanya\'nın en büyük karnaval geleneğini belgeleyen müze. Mainz Fastnacht, dünya genelinde tanınan renkli bir kültür mirasıdır.',
        'website': 'https://www.fastnachtsmuseum.de/',
        'maps_url': 'https://www.google.com/maps/search/Fastnachtsmuseum+Mainz+Eisgrubweg',
    },
    {
        'ad': 'Weinmarkt Mainz (Şarap Pazarı)',
        'adres': 'Liebfrauenplatz / Marktplatz, 55116 Mainz',
        'aciklama': 'Rheinhessen şaraplarının tadıldığı açık hava şarap pazarı. Her yıl yaz aylarında düzenlenir.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Weinmarkt+Mainz+Liebfrauenplatz',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        sehir  = Stadt.objects.get(slug='mainz')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return
    for veri in GEZI:
        Yer.objects.get_or_create(
            ad=veri['ad'], stadt=sehir,
            defaults={
                'eyalet':      eyalet,
                'scope':       'stadt',
                'tur':         'yer',
                'kategori':    'gezi',
                'sehir':       'Mainz',
                'adres':       veri['adres'],
                'aciklama':    veri['aciklama'],
                'kapak_resmi': '',
                'website':     veri.get('website', ''),
                'maps_url':    veri.get('maps_url', ''),
                'icerik':      '',
                'aktif':       True,
            }
        )


def unseed(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    sehir = Stadt.objects.filter(slug='mainz').first()
    if not sehir:
        return
    adlar = [v['ad'] for v in GEZI]
    Yer.objects.filter(ad__in=adlar, stadt=sehir).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0038_yer_sira_alani'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
