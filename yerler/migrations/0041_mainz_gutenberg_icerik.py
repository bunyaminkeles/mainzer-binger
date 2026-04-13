from django.db import migrations

GUTENBERG_ICERIK = """<h2>Gutenberg Müzesi — Bilgi Devriminin Merkezi</h2>

<p>Mainz, insanlık tarihinin en önemli buluşlarından biri olan <strong>hareketli parçalı matbaanın doğum yeridir</strong>. Johannes Gutenberg'in 1450 civarında kentin surları içinde gerçekleştirdiği bu devrim, Gutenberg Müzesi'nde tüm yönleriyle sergilenmektedir. Müze, sadece matbaa teknolojisini değil, yazılı kültürün ve kitap sanatının küresel gelişimini kronolojik bir perspektifle sunan bir <em>"Dünya Basım Sanatı Müzesi"</em> olarak tanımlanır.</p>

<h3>Ana Koleksiyon</h3>
<p>Müzenin koleksiyonunda yer alan 3.300'den fazla erken dönem baskı (<em>incunabula</em>) eser arasında, paha biçilemez <strong>iki adet orijinal Gutenberg İncili (42 satırlık İncil)</strong> bulunmaktadır. Bu eserler, teknik mükemmellikleri ve estetik detaylarıyla matbaanın sadece bir araç değil, aynı zamanda bir sanat formu olduğunu kanıtlar niteliktedir. Ziyaretçiler, 15. yüzyıl teknikleriyle çalışan bir matbaa makinesinde gerçekleştirilen <strong>canlı gösterilerle</strong> tarihin nasıl şekillendiğine tanıklık edebilmektedir.</p>

<table class="table table-sm table-bordered">
  <thead class="table-dark">
    <tr><th>Eser</th><th>Açıklama</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Gutenberg İncilleri</strong></td>
      <td>Dünyada yalnızca 49 adet kalan kopyadan ikisi burada muhafaza edilmektedir.</td>
    </tr>
    <tr>
      <td><strong>Hartmann Schedel Dünya Kroniği (1493)</strong></td>
      <td>Orta Çağ'ın sonundaki dünya bilgisini yüzlerce gravürle sunan anıtsal eser.</td>
    </tr>
    <tr>
      <td><strong>Blok Kitaplar ve El Yazmaları</strong></td>
      <td>Matbaa öncesi ve erken matbaa dönemine ait nadir dini ve bilimsel metinler.</td>
    </tr>
    <tr>
      <td><strong>Asya ve Uzak Doğu Baskı Sanatı</strong></td>
      <td>Doğu toplumlarının matbaa teknolojisindeki erken dönem katkılarını inceleyen özel bölümler.</td>
    </tr>
  </tbody>
</table>

<h3>Medya Kenti Mainz</h3>
<p>Müze, kentin medya kenti kimliğini güncel tutmakta ve her yıl binlerce araştırmacıyı ağırlamaktadır. Mainz'ın modern medya dünyasındaki konumu, Avrupa'nın en büyük televizyon yayıncılarından biri olan <strong>ZDF'nin merkezinin burada bulunmasıyla</strong> pekişmektedir.</p>"""

GUTENBERG_ACIKLAMA = (
    "Matbaacılığın mucidi Johannes Gutenberg'e adanmış dünya müzesi. "
    "Orijinal Gutenberg İncili ve 3.300+ erken dönem baskı eserin sergilendiği "
    "\"Dünya Basım Sanatı Müzesi\". Canlı matbaa gösterileri de yapılmaktadır."
)


def guncelle(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    sehir = Stadt.objects.filter(slug='mainz').first()
    if not sehir:
        return
    Yer.objects.filter(ad='Gutenberg-Museum', stadt=sehir).update(
        aciklama=GUTENBERG_ACIKLAMA,
        icerik=GUTENBERG_ICERIK,
    )


def geri_al(apps, schema_editor):
    Yer   = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')
    sehir = Stadt.objects.filter(slug='mainz').first()
    if not sehir:
        return
    Yer.objects.filter(ad='Gutenberg-Museum', stadt=sehir).update(
        aciklama=(
            "Matbaacılığın mucidi Johannes Gutenberg'e adanmış dünya müzesi. "
            "Orijinal Gutenberg İncili sergilenmektedir."
        ),
        icerik='',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0040_mainz_dom_icerik'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
