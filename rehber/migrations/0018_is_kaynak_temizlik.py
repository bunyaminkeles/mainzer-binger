"""
Resmi Kurum sekmesinden kaldırılan Kaynak kayıtları:
- Mainz Jobcenter
- HWK Rheinhessen — Göçmenler İçin
- Mainz Ausländerbehörde — Online Randevu
"""
from django.db import migrations

KALDIRILANLAR = [
    'Mainz Jobcenter',
    'HWK Rheinhessen — Göçmenler İçin',
    'Mainz Ausländerbehörde — Online Randevu',
]


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=False)


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=True)


class Migration(migrations.Migration):
    dependencies = [('rehber', '0017_egitim_kaynak_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
