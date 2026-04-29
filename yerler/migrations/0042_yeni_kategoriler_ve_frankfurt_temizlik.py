from django.db import migrations

def ileri(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')

    # Duplikat eski kayıtları sil
    for pk in [284, 282]:
        Yer.objects.filter(pk=pk).delete()

    # JSON'dan eklenen tüm Frankfurt gezi yerlerini gezi kategorisine al
    gezi_pkler = [283, 358, 359, 360, 361, 362, 363, 364, 365,
                  366, 367, 368, 369, 370, 371, 372, 373, 374, 375]
    Yer.objects.filter(pk__in=gezi_pkler).update(kategori='gezi')

def geri(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [('yerler', '0041_mainz_gutenberg_icerik')]
    operations = [migrations.RunPython(ileri, geri)]
