"""
Data migration:
- 16 Alman eyaletinin tümü eklenir (hepsi pasif, RLP aktif).
- Mevcut tüm Stadt kayıtları RLP'ye bağlanır.
"""
from django.db import migrations


EYALETLER = [
    {'ad': 'Baden-Württemberg',      'slug': 'bw',  'kod': 'BW', 'baskent': 'Stuttgart',   'aktif': False},
    {'ad': 'Bayern',                 'slug': 'by',  'kod': 'BY', 'baskent': 'München',      'aktif': False},
    {'ad': 'Berlin',                 'slug': 'be',  'kod': 'BE', 'baskent': 'Berlin',       'aktif': False},
    {'ad': 'Brandenburg',            'slug': 'bb',  'kod': 'BB', 'baskent': 'Potsdam',      'aktif': False},
    {'ad': 'Bremen',                 'slug': 'hb',  'kod': 'HB', 'baskent': 'Bremen',       'aktif': False},
    {'ad': 'Hamburg',                'slug': 'hh',  'kod': 'HH', 'baskent': 'Hamburg',      'aktif': False},
    {'ad': 'Hessen',                 'slug': 'he',  'kod': 'HE', 'baskent': 'Wiesbaden',    'aktif': False},
    {'ad': 'Mecklenburg-Vorpommern', 'slug': 'mv',  'kod': 'MV', 'baskent': 'Schwerin',     'aktif': False},
    {'ad': 'Niedersachsen',          'slug': 'ni',  'kod': 'NI', 'baskent': 'Hannover',     'aktif': False},
    {'ad': 'Nordrhein-Westfalen',    'slug': 'nw',  'kod': 'NW', 'baskent': 'Düsseldorf',   'aktif': False},
    {'ad': 'Rheinland-Pfalz',        'slug': 'rlp', 'kod': 'RP', 'baskent': 'Mainz',        'aktif': True},
    {'ad': 'Saarland',               'slug': 'sl',  'kod': 'SL', 'baskent': 'Saarbrücken',  'aktif': False},
    {'ad': 'Sachsen',                'slug': 'sn',  'kod': 'SN', 'baskent': 'Dresden',      'aktif': False},
    {'ad': 'Sachsen-Anhalt',         'slug': 'st',  'kod': 'ST', 'baskent': 'Magdeburg',    'aktif': False},
    {'ad': 'Schleswig-Holstein',     'slug': 'sh',  'kod': 'SH', 'baskent': 'Kiel',         'aktif': False},
    {'ad': 'Thüringen',              'slug': 'th',  'kod': 'TH', 'baskent': 'Erfurt',       'aktif': False},
]


def seed_eyaletler(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')

    for e in EYALETLER:
        Eyalet.objects.get_or_create(slug=e['slug'], defaults=e)

    # Mevcut tüm şehirleri RLP'ye bağla
    rlp = Eyalet.objects.get(slug='rlp')
    Stadt.objects.filter(eyalet__isnull=True).update(eyalet=rlp)


def reverse_seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.all().update(eyalet=None)
    slugs = [e['slug'] for e in EYALETLER]
    Eyalet.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0007_eyalet_model_stadt_fk'),
    ]

    operations = [
        migrations.RunPython(seed_eyaletler, reverse_seed),
    ]
