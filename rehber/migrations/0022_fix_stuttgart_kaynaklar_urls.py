from django.db import migrations

FIXES = [
    {
        'baslik': 'Stuttgart Bürgerbüro — Online Termin',
        'url': 'https://stuttgart.konsentas.de/form/1/?signup_new=1',
    },
    {
        'baslik': 'Stuttgart Ausländerbehörde',
        'url': 'https://stuttgart.konsentas.de/form/7/?signup_new=1',
    },
    {
        'baslik': 'Caritas Stuttgart — Göçmen Danışmanlığı',
        'url': 'https://www.caritas-stuttgart.de/hilfe-beratung/migration-integration-und-flucht/',
    },
    {
        'baslik': 'Jobcenter Stuttgart',
        'url': 'https://www.stuttgart.de/leben/arbeit/jobcenter',
    },
]


def fix_urls(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    for fix in FIXES:
        Kaynak.objects.filter(baslik=fix['baslik']).update(url=fix['url'])


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0021_seed_stuttgart_kaynaklar'),
    ]

    operations = [
        migrations.RunPython(fix_urls, migrations.RunPython.noop),
    ]
