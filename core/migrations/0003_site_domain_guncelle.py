from django.db import migrations


def site_domain_guncelle(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.filter(id=1).update(
        domain='almanyalirehber.com',
        name='Almanyalı Rehber',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_siteziyaret'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(site_domain_guncelle, migrations.RunPython.noop),
    ]
