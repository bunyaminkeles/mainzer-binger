"""
Data migration: 404 ve bağlanamayan kırık linkler Kaynak ve OnemliLink'ten silinir.

Kırık:
- BAMF WebGIS (404)
- BAMF MBE node (404)
- Bundesagentur Kindergeld (404)
- mieterbund-rlp.de (bağlantı yok)
- vhs-mainz-bingen.de (bağlantı yok)
"""
from django.db import migrations

KIRIK_SLUGLAR = [
    'bamf-integrationskurs-bul',
    'mbe-migrationsberatung',
    'kindergeld-basvuru',
    'mieterbund-rlp',
    'vhs-mainz-bingen',
]

KIRIK_URLLER = [
    'https://www.bamf.de/SiteGlobals/Functions/WebGIS/DE/WebGIS_Integrationskurs.html',
    'https://www.bamf.de/DE/Themen/Beratung/MBE/mbe-node.html',
    'https://www.arbeitsagentur.de/familie-und-kinder/kindergeld-beantragen',
    'https://www.mieterbund-rlp.de/',
    'https://www.vhs-mainz-bingen.de/',
]


def sil(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Kaynak.objects.filter(slug__in=KIRIK_SLUGLAR).delete()
    OnemliLink.objects.filter(url__in=KIRIK_URLLER).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0005_entegrasyon_kaynaklari'),
        ('linkler', '0004_entegrasyon_linkleri'),
    ]

    operations = [
        migrations.RunPython(sil, migrations.RunPython.noop),
    ]
