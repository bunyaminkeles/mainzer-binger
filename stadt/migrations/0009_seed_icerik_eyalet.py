"""
Data migration: Tüm içerik modellerindeki kayıtları Eyalet FK'ına bağla.
- scope='eyalet' → RLP eyaletine ata
- scope='stadt'  → o şehrin eyaletine ata (stadt.eyalet üzerinden)
"""
from django.db import migrations


MODELLER = [
    ('duyurular', 'Duyuru'),
    ('blog',      'BlogYazisi'),
    ('forum',     'Konu'),
    ('ilan',      'Ilan'),
    ('rehber',    'Kaynak'),
    ('takvim',    'Etkinlik'),
    ('linkler',   'OnemliLink'),
    ('yerler',    'Yer'),
]


def icerik_eyalet_ata(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')

    try:
        rlp = Eyalet.objects.get(slug='rlp')
    except Eyalet.DoesNotExist:
        return

    for app_label, model_name in MODELLER:
        Model = apps.get_model(app_label, model_name)

        # scope='eyalet' → RLP
        Model.objects.filter(scope='eyalet', eyalet__isnull=True).update(eyalet=rlp)

        # scope='stadt' → şehrin eyaleti
        for stadt in Stadt.objects.filter(eyalet__isnull=False).select_related('eyalet'):
            Model.objects.filter(
                scope='stadt', stadt=stadt, eyalet__isnull=True
            ).update(eyalet=stadt.eyalet)


def geri_al(apps, schema_editor):
    for app_label, model_name in MODELLER:
        Model = apps.get_model(app_label, model_name)
        Model.objects.all().update(eyalet=None)


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0008_seed_eyaletler'),
        ('duyurular', '0007_eyalet_fk'),
        ('blog',      '0010_eyalet_fk'),
        ('forum',     '0007_eyalet_fk'),
        ('ilan',      '0005_eyalet_fk'),
        ('rehber',    '0012_eyalet_fk'),
        ('takvim',    '0004_eyalet_fk'),
        ('linkler',   '0006_eyalet_fk'),
        ('yerler',    '0011_eyalet_fk'),
    ]

    operations = [
        migrations.RunPython(icerik_eyalet_ata, geri_al),
    ]
