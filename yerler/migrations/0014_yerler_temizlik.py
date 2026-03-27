"""
Eğitim ve Resmi Kurum sekmeleri — fazla/yanlış kayıt temizliği:
- Kreisverwaltung Mainz-Bingen — Ausländerbehörde: Ausländerbehörde Mainz yeterli
- Finanzamt Bingen-Alzey: yerler listesinden çıkarılıyor
- Berlitz Sprachschule, Hochschule Mainz (FH): kaldırılıyor
- ABC / Akademisches Bildungs-Center varyantı: kaldırılıyor (ABC Sprachschule Mainz kalacak)
- JGU "Mainz" eklenmiş varyantı dışındaki giriş: kaldırılıyor
- KFZ-Zulassungsstelle duplikat: kaldırılıyor
"""
from django.db import migrations


KALDIRILANLAR_EGITIM = [
    'Berlitz Sprachschule Mainz',
    'Berlitz Sprachschule',
    'Hochschule Mainz (FH)',
    'Hochschule Mainz',
]

KALDIRILANLAR_RESMI = [
    'Kreisverwaltung Mainz-Bingen — Ausländerbehörde',
    'Finanzamt Bingen-Alzey',
]


def guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')

    # Kesin isimle devre dışı
    Yer.objects.filter(
        ad__in=KALDIRILANLAR_EGITIM, kategori='egitim'
    ).update(aktif=False)

    Yer.objects.filter(
        ad__in=KALDIRILANLAR_RESMI, kategori='resmi_kurum'
    ).update(aktif=False)

    # ABC Sprachschule Mainz kalacak, Akademisches Bildungs-Center varyantı devre dışı
    Yer.objects.filter(
        ad__icontains='Akademisches Bildungs-Center', kategori='egitim'
    ).update(aktif=False)

    # Johannes Gutenberg-Universität Mainz kalacak, diğer varyantlar devre dışı
    Yer.objects.filter(
        ad__icontains='Johannes Gutenberg', kategori='egitim'
    ).exclude(ad='Johannes Gutenberg-Universität Mainz').update(aktif=False)

    # KFZ-Zulassungsstelle Mainz kalacak, diğer varyantlar devre dışı
    Yer.objects.filter(
        ad__icontains='KFZ-Zulassungsstelle', kategori='resmi_kurum'
    ).exclude(ad='KFZ-Zulassungsstelle Mainz').update(aktif=False)


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(
        ad__in=KALDIRILANLAR_EGITIM, kategori='egitim'
    ).update(aktif=True)
    Yer.objects.filter(
        ad__in=KALDIRILANLAR_RESMI, kategori='resmi_kurum'
    ).update(aktif=True)
    Yer.objects.filter(
        ad__icontains='Akademisches Bildungs-Center', kategori='egitim'
    ).update(aktif=True)
    Yer.objects.filter(
        ad__icontains='Johannes Gutenberg', kategori='egitim'
    ).exclude(ad='Johannes Gutenberg-Universität Mainz').update(aktif=True)
    Yer.objects.filter(
        ad__icontains='KFZ-Zulassungsstelle', kategori='resmi_kurum'
    ).exclude(ad='KFZ-Zulassungsstelle Mainz').update(aktif=True)


class Migration(migrations.Migration):
    dependencies = [('yerler', '0013_mainz_resmi_egitim_guncelle')]
    operations = [migrations.RunPython(guncelle, geri_al)]
