from django.db import migrations


def guncelle(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')

    BlogYazisi.objects.filter(slug='helau-mainz-karnavali-nedir').update(
        kapak_resmi='/static/img/blog/helau.jpeg',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_zulassung_mainze_tasi'),
    ]

    operations = [
        migrations.RunPython(guncelle, migrations.RunPython.noop),
    ]
