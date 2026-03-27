"""
Resmi Kurum sekmesinden kaldırılan Kaynak (link) kayıtları:
- Bundesagentur für Arbeit
- Elterngeld — Doğum Parası Başvurusu
- Make it in Germany — Türkçe Çalışma Rehberi
- Antidiskriminierungsstelle des Bundes
"""
from django.db import migrations

KALDIRILANLAR = [
    'Bundesagentur für Arbeit',
    'Elterngeld — Doğum Parası Başvurusu',
    'Make it in Germany — Türkçe Çalışma Rehberi',
    'Antidiskriminierungsstelle des Bundes',
]


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=False)


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=True)


class Migration(migrations.Migration):
    dependencies = [('rehber', '0015_kaynak_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
