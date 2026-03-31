# Generated manually
from django.db import migrations

def seed_yeni_belgeler(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')

    YENI_BELGELER = [
        {
            'baslik': 'Almanya Meslekler Listesi (Berufe in Deutschland)',
            'kategori': 'genel',
            'harici_link': '/media/belgeler/Berufe_List_in_Deutschland-1.pdf',
            'ozet': 'Almanya\'daki resmi mesleklerin listesi ve detayları.',
            'yayinda': True,
        },
        {
            'baslik': 'Staj Haftası Çalışma Kağıdı (Praktikumswoche)',
            'kategori': 'genel',
            'harici_link': '/media/belgeler/arbeitsblatt-praktikumswoche.pdf',
            'ozet': 'Öğrenciler ve yeni mezunlar için staj (Praktikum) haftası değerlendirme formu.',
            'yayinda': True,
        },
    ]

    for d in YENI_BELGELER:
        Belge.objects.get_or_create(
            baslik=d['baslik'],
            stadt=None,
            defaults={
                'kategori': d['kategori'],
                'harici_link': d['harici_link'],
                'ozet': d['ozet'],
                'yayinda': d['yayinda']
            }
        )

class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0033_ajet_kaldir'),
    ]
    operations = [
        migrations.RunPython(seed_yeni_belgeler, migrations.RunPython.noop),
    ]