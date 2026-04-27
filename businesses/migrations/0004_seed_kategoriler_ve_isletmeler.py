from django.db import migrations
import datetime

KATEGORILER = [
    {'slug': 'market-gida',       'name': 'Türk Market & Gıda',       'icon': 'basket2'},
    {'slug': 'restoran-kafe',     'name': 'Restoran & Kafe',           'icon': 'cup-hot'},
    {'slug': 'hukuk-danismanlik', 'name': 'Hukuk & Danışmanlık',      'icon': 'briefcase'},
    {'slug': 'berber-kuafor',     'name': 'Berber & Kuaför',           'icon': 'scissors'},
    {'slug': 'muhasebe-vergi',    'name': 'Muhasebe & Vergi',          'icon': 'calculator'},
    {'slug': 'sigorta',           'name': 'Sigorta',                   'icon': 'shield-check'},
    {'slug': 'nakliyat',          'name': 'Nakliyat & Taşımacılık',    'icon': 'truck'},
]

ISLETMELER = [
    # Mainz
    {
        'name': 'Can Market Mainz',
        'slug': 'can-market-mainz',
        'stadt_slug': 'mainz',
        'kategori_slug': 'market-gida',
        'slogan': 'Mainz\'in kalbinde helal Türk ürünleri',
        'description': 'Mainz merkezde helal et, Türk gıda ürünleri ve taze sebze-meyve. Her gün açık.',
        'whatsapp_number': '+4917600000001',
        'is_verified': True,
    },
    {
        'name': 'Avukat Mehmet Yıldız',
        'slug': 'avukat-mehmet-yildiz-mainz',
        'stadt_slug': 'mainz',
        'kategori_slug': 'hukuk-danismanlik',
        'slogan': 'Türkçe hukuki danışmanlık — göçmenlik, iş ve aile hukuku',
        'description': 'Mainz\'de 15 yıllık deneyimle Türkçe hukuk danışmanlığı. İlk görüşme ücretsiz.',
        'whatsapp_number': '+4917600000002',
        'is_verified': True,
    },
    {
        'name': 'Ankara Döner & Grill',
        'slug': 'ankara-doner-grill-mainz',
        'stadt_slug': 'mainz',
        'kategori_slug': 'restoran-kafe',
        'slogan': 'Geleneksel Türk lezzetleri — Mainz\'de 20 yıldır',
        'description': 'Adana kebap, lahmacun, pide ve döner. Aile ortamında ev yemeği tadında.',
        'whatsapp_number': '+4917600000003',
        'is_verified': False,
    },

    # Köln
    {
        'name': 'Bosphorus Market Köln',
        'slug': 'bosphorus-market-koeln',
        'stadt_slug': 'koeln',
        'kategori_slug': 'market-gida',
        'slogan': 'Köln Ehrenfeld\'de geniş Türk & Orta Doğu ürünleri',
        'description': 'Helal et, taze meze, Türk peynir çeşitleri ve ithal baharatlar.',
        'whatsapp_number': '+4917600000004',
        'is_verified': True,
    },
    {
        'name': 'Berber Ahmet — Köln',
        'slug': 'berber-ahmet-koeln',
        'stadt_slug': 'koeln',
        'kategori_slug': 'berber-kuafor',
        'slogan': 'Klasik Türk berberi deneyimi — randevusuz hizmet',
        'description': 'Saç, sakal ve cilt bakımı. Rahat ortam, Türkçe sohbet.',
        'whatsapp_number': '+4917600000005',
        'is_verified': False,
    },

    # Frankfurt
    {
        'name': 'Anadolu Nakliyat Frankfurt',
        'slug': 'anadolu-nakliyat-frankfurt',
        'stadt_slug': 'frankfurt',
        'kategori_slug': 'nakliyat',
        'slogan': 'Frankfurt\'ta ev ve ofis taşıma — Türkçe iletişim',
        'description': 'Sigortalı taşıma, ambalajlama ve montaj hizmeti. Hafta sonları da çalışıyoruz.',
        'whatsapp_number': '+4917600000006',
        'is_verified': True,
    },
    {
        'name': 'Yılmaz Muhasebe Bürosu',
        'slug': 'yilmaz-muhasebe-frankfurt',
        'stadt_slug': 'frankfurt',
        'kategori_slug': 'muhasebe-vergi',
        'slogan': 'Vergi beyannamesi ve serbest meslek muhasebesi — Türkçe',
        'description': 'Steuererklärung, Gewerbeanmeldung, Buchhaltung. Randevuyla veya WhatsApp\'tan ulaşın.',
        'whatsapp_number': '+4917600000007',
        'is_verified': True,
    },

    # Hamburg
    {
        'name': 'İstanbul Süpermarket Hamburg',
        'slug': 'istanbul-supermarket-hamburg',
        'stadt_slug': 'hamburg',
        'kategori_slug': 'market-gida',
        'slogan': 'Hamburg\'da en büyük Türk market zinciri',
        'description': 'Helal et reyonu, fırın, hazır yemek ve Türkiye\'den ithal ürünler.',
        'whatsapp_number': '+4917600000008',
        'is_verified': True,
    },
    {
        'name': 'Sigorta Danışmanı Ali Demir',
        'slug': 'sigorta-ali-demir-hamburg',
        'stadt_slug': 'hamburg',
        'kategori_slug': 'sigorta',
        'slogan': 'Kranken, Haftpflicht, KFZ — Türkçe sigorta danışmanlığı',
        'description': 'Almanya\'da sigorta seçimi kafa karıştırıcı olabilir. Türkçe açıklıyoruz, doğru paketi buluyoruz.',
        'whatsapp_number': '+4917600000009',
        'is_verified': False,
    },

    # Düsseldorf
    {
        'name': 'Golden Berber Düsseldorf',
        'slug': 'golden-berber-dusseldorf',
        'stadt_slug': 'duesseldorf',
        'kategori_slug': 'berber-kuafor',
        'slogan': 'Modern saç & sakal şekillendirme — Türkçe hizmet',
        'description': 'Düsseldorf Oberbilk\'te. Saç kesimi, ombre, keratin ve cilt bakımı.',
        'whatsapp_number': '+4917600000010',
        'is_verified': True,
    },

    # Wiesbaden
    {
        'name': 'Wiesbaden Türk Evi Market',
        'slug': 'wiesbaden-turk-evi-market',
        'stadt_slug': 'wiesbaden',
        'kategori_slug': 'market-gida',
        'slogan': 'Wiesbaden\'da helal et ve Türk gıdası',
        'description': 'Haftanın 7 günü açık. Özel sipariş ve toplu alım imkânı.',
        'whatsapp_number': '+4917600000011',
        'is_verified': False,
    },
]


def ekle(apps, schema_editor):
    BusinessCategory = apps.get_model('businesses', 'BusinessCategory')
    LocalBusiness = apps.get_model('businesses', 'LocalBusiness')
    SubscriptionPlan = apps.get_model('businesses', 'SubscriptionPlan')
    Stadt = apps.get_model('stadt', 'Stadt')

    # Kategoriler
    for kat in KATEGORILER:
        BusinessCategory.objects.get_or_create(
            slug=kat['slug'],
            defaults={'name': kat['name'], 'icon': kat['icon']},
        )

    # Varsayılan abonelik planı
    plan, _ = SubscriptionPlan.objects.get_or_create(
        name='Standart',
        defaults={'price': 29.90, 'duration_days': 365, 'is_active': True},
    )

    bitis = datetime.date(2027, 12, 31)

    for veri in ISLETMELER:
        try:
            stadt = Stadt.objects.get(slug=veri['stadt_slug'])
        except Stadt.DoesNotExist:
            continue

        try:
            kategori = BusinessCategory.objects.get(slug=veri['kategori_slug'])
        except BusinessCategory.DoesNotExist:
            continue

        LocalBusiness.objects.get_or_create(
            slug=veri['slug'],
            defaults={
                'name': veri['name'],
                'city': stadt,
                'category': kategori,
                'slogan': veri.get('slogan', ''),
                'description': veri.get('description', ''),
                'whatsapp_number': veri.get('whatsapp_number', ''),
                'subscription_plan': plan,
                'start_date': datetime.date(2026, 1, 1),
                'end_date': bitis,
                'is_published': True,
                'is_verified': veri.get('is_verified', False),
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0003_logo_cover_url_fields'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
