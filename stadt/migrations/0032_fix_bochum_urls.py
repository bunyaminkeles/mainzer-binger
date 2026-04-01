"""
Bochum: termin_url, auslaenderbehorde_url ve rss_duyuru_url düzeltmesi.
"""
from django.db import migrations


def fix(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='bochum').update(
        termin_url='https://www.bochum.de/Online-Terminbuchung',
        auslaenderbehorde_url='https://www.bochum.de/Auslaenderbuero',
        rss_duyuru_url='https://www.bochum.de/neu/BODirector.nsf/DIRECTOR.xsp?qname=RSS_Pressemeldungen&q=2_&type=1&lg=DE',
    )


def unfix(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0031_seed_bochum'),
    ]

    operations = [
        migrations.RunPython(fix, unfix),
    ]
