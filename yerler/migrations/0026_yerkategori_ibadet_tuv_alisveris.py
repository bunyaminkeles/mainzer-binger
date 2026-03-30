from django.db import migrations


def seed(apps, schema_editor):
    YerKategori = apps.get_model('yerler', 'YerKategori')
    for d in [
        dict(slug='ibadet',    ad='İbadet',    tur='yer', sira=4),
        dict(slug='tuv',       ad='TÜV / Muayene', tur='yer', sira=5),
        dict(slug='alisveris', ad='Alışveriş', tur='yer', sira=6),
    ]:
        YerKategori.objects.get_or_create(slug=d['slug'], defaults=d)


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0025_seed_worms_yerler'),
    ]
    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
