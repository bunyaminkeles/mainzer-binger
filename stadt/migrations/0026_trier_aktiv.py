from django.db import migrations


def aktivlestir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='trier').update(aktiv=True)


def geri_al(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='trier').update(aktiv=False)


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0025_trier_action_links'),
    ]
    operations = [
        migrations.RunPython(aktivlestir, geri_al),
    ]
