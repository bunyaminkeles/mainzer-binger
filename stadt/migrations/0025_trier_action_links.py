from django.db import migrations

CITY_DATA = {
    'trier': {
        'termin_url':            'https://www.trier.de/rathaus-buerger-in/buergerservice/terminvereinbarung/',
        'auslaenderbehorde_url': 'https://www.trier.de/rathaus-buerger-in/stadtverwaltung/aemter-dienststellen/dezernat-ii/amt-fuer-auslaenderfragen/',
        'rss_duyuru_url':        'https://www.trier.de/aktuelles/nachrichten/',
    },
}


def update_cities(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    for slug, data in CITY_DATA.items():
        try:
            sehir = Stadt.objects.get(slug=slug)
            sehir.termin_url            = data['termin_url']
            sehir.auslaenderbehorde_url = data['auslaenderbehorde_url']
            sehir.rss_duyuru_url        = data['rss_duyuru_url']
            sehir.save()
        except Stadt.DoesNotExist:
            continue


def reverse_update(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0024_ludwigshafen_aktiv'),
    ]
    operations = [
        migrations.RunPython(update_cities, reverse_update),
    ]
