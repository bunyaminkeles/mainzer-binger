"""
- NW eyaletini aktif yap
- Frankenthal'i aktiv yap
- Bochum: doğru NW eyaletine bağla, population/lat/lng güncelle
"""
from django.db import migrations


def fix(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')

    # 1. NW eyaletini aktif yap
    nw = Eyalet.objects.filter(slug='nw', kod='NW').first()
    if nw:
        nw.aktif = True
        nw.save(update_fields=['aktif'])

    # 2. Frankenthal aktiv yap
    Stadt.objects.filter(slug='frankenthal').update(aktiv=True)

    # 3. Bochum: yanlış eyalete bağlıysa düzelt, eksik alanları doldur
    if nw:
        Stadt.objects.filter(slug='bochum').update(
            eyalet=nw,
            population=365000,
            lat=51.4818,
            lng=7.2162,
        )


def unfix(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0032_fix_bochum_urls'),
    ]

    operations = [
        migrations.RunPython(fix, unfix),
    ]
