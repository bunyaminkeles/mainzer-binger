"""
Bochum Kaynak URL düzeltmeleri + mükerrer kayıtların temizlenmesi.
- Ausländerbehörde, Online Termin, KdU URL'leri düzeltildi
- Ausländerbehörde Kaynak kaldırıldı (Yer olarak zaten mevcut)
- Bürger-Service-Center Yer kaldırıldı (Ausländerbehörde ile aynı adreste, gereksiz)
"""
from django.db import migrations


def fix(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Yer    = apps.get_model('yerler', 'Yer')
    Stadt  = apps.get_model('stadt', 'Stadt')

    try:
        bochum = Stadt.objects.get(slug='bochum')
    except Stadt.DoesNotExist:
        return

    # 1. Ausländerbehörde Kaynak'ı kaldır (Yer olarak zaten var)
    Kaynak.objects.filter(stadt=bochum, baslik='Ausländerbehörde Bochum').delete()

    # 2. Online Termin URL düzelt
    Kaynak.objects.filter(stadt=bochum, baslik='Online Termin — Bochum Belediyesi').update(
        url='https://www.bochum.de/Online-Terminbuchung'
    )

    # 3. KdU URL düzelt
    Kaynak.objects.filter(stadt=bochum, baslik='Bochum KdU — Kosten der Unterkunft').update(
        url='https://www.bochum.de/media/Bedarfe-fuer-Unterkunft-und-Heizung---Verfuegungssammlung-Version-SGB-II'
    )

    # 4. Bürger-Service-Center Yer'ini kaldır (Ausländerbehörde ile aynı binada, mükerrer)
    Yer.objects.filter(stadt=bochum, ad='Bürger-Service-Center Bochum').delete()


def unfix(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0033_nw_aktif_frankenthal_bochum_fix'),
        ('rehber', '0034_yeni_belgeler_ekle'),
        ('yerler', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fix, unfix),
    ]
