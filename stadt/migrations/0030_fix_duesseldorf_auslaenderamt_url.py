from django.db import migrations


def fix(apps, schema_editor):
    Stadt  = apps.get_model('stadt', 'Stadt')
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Yer    = apps.get_model('yerler', 'Yer')

    DOGRU = 'https://www.duesseldorf.de/auslaenderamt'
    YANLIS = 'https://www.duesseldorf.de/auslaenderbehoerde'

    Stadt.objects.filter(slug='duesseldorf').update(auslaenderbehorde_url=DOGRU)
    Kaynak.objects.filter(url=YANLIS).update(url=DOGRU)
    Yer.objects.filter(website=YANLIS).update(website=DOGRU)


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0029_seed_duesseldorf'),
    ]

    operations = [
        migrations.RunPython(fix, migrations.RunPython.noop),
    ]
