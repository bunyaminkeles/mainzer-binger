"""
Mainz Resmi Kurum + Eğitim sekmeleri için veri düzenlemesi:
- Finanzamt Mainz-Stadt devre dışı
- Agentur für Arbeit, Jobcenter, KFZ-Zulassungsstelle eklendi
- ABC Sprachschule, JGU, Sprachzentrum ProfiL eklendi
"""
from django.db import migrations


def guncelle(apps, schema_editor):
    Yer    = apps.get_model('yerler', 'Yer')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Eyalet = apps.get_model('stadt', 'Eyalet')

    mainz = Stadt.objects.filter(slug='mainz').first()
    rlp   = Eyalet.objects.filter(slug='rlp').first()
    if not mainz or not rlp:
        return

    # Finanzamt Mainz-Stadt devre dışı
    Yer.objects.filter(ad='Finanzamt Mainz-Stadt', stadt=mainz).update(aktif=False)

    # Eklenecek yerler
    YERLER = [
        # resmi_kurum
        dict(ad='Agentur für Arbeit Mainz',    kategori='resmi_kurum',
             adres='Parcusstraße 4, 55116 Mainz',
             website='https://www.arbeitsagentur.de/vor-ort/mainz/',
             maps_url='https://maps.google.com/?q=Parcusstra%C3%9Fe+4,+55116+Mainz'),
        dict(ad='Jobcenter Mainz',              kategori='resmi_kurum',
             adres='Kaiserstraße 26-28, 55116 Mainz',
             website='https://www.jobcenter-mainz.de/',
             maps_url='https://maps.google.com/?q=Kaiserstra%C3%9Fe+26,+55116+Mainz'),
        dict(ad='KFZ-Zulassungsstelle Mainz',  kategori='resmi_kurum',
             adres='Schillerstraße 1, 55116 Mainz',
             website='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/kfz-zulassung.php',
             maps_url='https://maps.google.com/?q=Schillerstrae+1,+55116+Mainz'),
        # egitim
        dict(ad='ABC Sprachschule Mainz',       kategori='egitim',
             adres='Große Bleiche 29-31, 55116 Mainz',
             website='https://www.abc-sprachschule.de/',
             maps_url='https://maps.google.com/?q=Gro%C3%9Fe+Bleiche+29,+55116+Mainz'),
        dict(ad='Johannes Gutenberg-Universität Mainz', kategori='egitim',
             adres='Saarstraße 21, 55122 Mainz',
             website='https://www.uni-mainz.de/',
             maps_url='https://maps.google.com/?q=Saarstra%C3%9Fe+21,+55122+Mainz'),
        dict(ad='Sprachzentrum ProfiL Mainz',   kategori='egitim',
             adres='Kaiserstraße 38, 55116 Mainz',
             website='https://www.profil-mainz.de/',
             maps_url='https://maps.google.com/?q=Kaiserstra%C3%9Fe+38,+55116+Mainz'),
    ]
    for v in YERLER:
        if not Yer.objects.filter(ad=v['ad'], stadt=mainz).exists():
            Yer.objects.create(
                tur='yer', scope='stadt', eyalet=rlp, stadt=mainz, aktif=True, **v
            )


def geri_al(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    mainz = Stadt.objects.filter(slug='mainz').first()
    if not mainz:
        return
    Yer.objects.filter(ad='Finanzamt Mainz-Stadt', stadt=mainz).update(aktif=True)
    eklenenlerin_adlari = [
        'Agentur für Arbeit Mainz', 'Jobcenter Mainz', 'KFZ-Zulassungsstelle Mainz',
        'ABC Sprachschule Mainz', 'Johannes Gutenberg-Universität Mainz',
        'Sprachzentrum ProfiL Mainz',
    ]
    Yer.objects.filter(ad__in=eklenenlerin_adlari, stadt=mainz).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0012_seed_wiesbaden_gezi'),
        ('stadt',  '0010_seed_baskentler'),
    ]
    operations = [migrations.RunPython(guncelle, geri_al)]
