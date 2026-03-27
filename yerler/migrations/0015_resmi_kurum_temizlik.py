"""
Resmi Kurum sekmesinden kaldırılanlar:
- Ausländerbehörde Mainz (Kreisverwaltung varyantı zaten pasifti)
- Finanzamt Mainz, Standesamt Mainz, Mainz Rathaus (üretim kayıtları)
"""
from django.db import migrations

KALDIRILANLAR = [
    'Ausländerbehörde Mainz',
    'Finanzamt Mainz',
    'Finanzamt Mainz (Vergi Dairesi)',
    'Standesamt Mainz',
    'Standesamt Mainz (Nüfus Müdürlüğü)',
    'Mainz Rathaus',
    'Mainz Rathaus (Stadthaus)',
]


def guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='resmi_kurum').update(aktif=False)


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='resmi_kurum').update(aktif=True)


class Migration(migrations.Migration):
    dependencies = [('yerler', '0014_yerler_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
