"""
Resmi Kurum ve Eğitim sekmesi için Kaynak temizliği:
- Listede olmayan kaynaklar devre dışı
- Caritas Mainz + Mainz Şehir Portalı yeniden aktif
"""
from django.db import migrations

KALDIR = [
    'KAUSA RLP — Ausbildung ve Göç Danışmanlığı',
    'Anabin Karar Aracı — ZAB Gerekli mi?',
    'Antidiskriminierungsstelle — Ayrımcılık Şikayeti',
    'BAMF — Göç ve Mülteci Dairesi',
    'Mainz Bürgeramt — Online Randevu',
    'SCHUFA Datenkopie — Ücretsiz Kredi Raporu',
    'Verbraucherzentrale Rheinland-Pfalz',
    'ZAB — Yabancı Diploma Değerlendirmesi',
    'Almanca Kurs Haritası',
    'Leben in Deutschland — Sınav Soruları (BAMF)',
]

AKTIF_ET = [
    'Caritas Mainz — Göçmen Danışmanlığı',
    'Mainz Şehir Portalı',
]


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIR).update(yayinda=False)
    Kaynak.objects.filter(baslik__in=AKTIF_ET).update(yayinda=True)


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIR).update(yayinda=True)
    Kaynak.objects.filter(baslik__in=AKTIF_ET).update(yayinda=False)


class Migration(migrations.Migration):
    dependencies = [('rehber', '0014_eksik_kaynaklar')]
    operations = [migrations.RunPython(guncelle, geri_al)]
