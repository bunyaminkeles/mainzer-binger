from django.db import migrations

DOM_ICERIK = """<h2>Aziz Martin Katedrali (Mainzer Dom)</h2>

<p>Mainz'ın silüetine bin yılı aşkın bir süredir hükmeden <strong>Aziz Martin Katedrali (Hoher Dom St. Martin)</strong>, Romanesk mimarinin Avrupa'daki en seçkin örneklerinden biri olarak kabul edilir. Başpiskopos Willigis tarafından 975 yılında inşasına başlanan yapı, kentin kalbindeki Pazar Meydanı'nda (Marktplatz) yükselmektedir. Katedralin karakteristik <strong>kırmızı kumtaşı cephesi</strong> ve altı kulesi, kentin "Altın Mainz" (Aurea Moguntia) olarak anılmasının en somut nedenidir.</p>

<h3>Mimari</h3>
<p>Katedralin mimari yapısı, yüzyıllar boyunca süren eklemeler ve restorasyonlar nedeniyle <strong>Romanesk, Gotik ve Barok</strong> unsurların büyüleyici bir sentezini sunar. İç mekânda kentin dini ve siyasi tarihini yansıtan başpiskoposların görkemli mezarları, heybetli tonozlar ve Nazarene hareketine ait dini duvar resimleri dikkat çekicidir. Katedral, tarih boyunca yedi kraliyet taç giyme törenine ev sahipliği yaparak kentin imparatorluk içindeki önemini pekiştirmiştir.</p>

<table class="table table-sm table-bordered">
  <thead class="table-dark">
    <tr><th>Mimari Unsur / Dönem</th><th>Özellik ve Gelişme</th></tr>
  </thead>
  <tbody>
    <tr><td>Erken Romanesk (1009)</td><td>Willigis Katedrali'nin açılış gününde yangınla tahribi.</td></tr>
    <tr><td>Kuleler ve Çatılar (1767)</td><td>Batı kulesinin yıldırım çarpması sonucu Barok tarzda yenilenmesi.</td></tr>
    <tr><td>Modern Güçlendirme (1909–1928)</td><td>Temellerin beton ve çelik ile takviye edilmesi.</td></tr>
    <tr><td>Piskoposluk Müzesi</td><td>Hazinedeki dini sanat eserleri ve el yazmaları.</td></tr>
  </tbody>
</table>

<h3>Marktplatz ve "Weck, Worscht un Woi" Geleneği</h3>
<p>Katedralin hemen yanındaki <strong>Pazar Meydanı (Marktplatz)</strong>, haftanın üç günü (Salı, Cuma, Cumartesi) kurulan renkli pazarıyla kentin sosyal yaşamının merkezidir. Buradaki <em>Marktfrühstück</em> (Pazar Kahvaltısı) geleneği, yerel şarap üreticilerinin sunduğu şaraplar ve <strong>"Weck, Worscht un Woi"</strong> (ekmek, sosis ve şarap) üçlüsüyle Mainz kültürünün en samimi ifadesidir.</p>"""

DOM_ACIKLAMA = (
    "Mainz'ın simgesi, 975 yılında temeli atılan Romanesk katedrali. "
    "Kırmızı kumtaşı cephesi ve altı kulesiyle şehrin siluetine hükmeder. "
    "Mainz Başpiskoposluğu'nun merkezi; 7 kraliyet taç giyme törenine ev sahipliği yapmıştır."
)


def guncelle(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    sehir = Stadt.objects.filter(slug='mainz').first()
    if not sehir:
        return
    Yer.objects.filter(ad='Mainzer Dom (Hoher Dom St. Martin)', stadt=sehir).update(
        aciklama=DOM_ACIKLAMA,
        icerik=DOM_ICERIK,
    )


def geri_al(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    sehir = Stadt.objects.filter(slug='mainz').first()
    if not sehir:
        return
    Yer.objects.filter(ad='Mainzer Dom (Hoher Dom St. Martin)', stadt=sehir).update(
        aciklama='Mainz\'ın simgesi, 1000 yıllık Romanesk katedrali. Mainz Başpiskoposluğu\'nun merkezi ve UNESCO mirası.',
        icerik='',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0039_mainz_gezi_guncelle'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
