from django.db import migrations

ICERIK = """
<p>Bahar aylarının gelmesiyle birlikte Almanya'daki süpermarket raflarını çikolatadan tavşanların ve rengarenk boyanmış yumurtaların süslediğini fark etmişsinizdir. Almanya'da yaşayanlar veya buraya yeni taşınanlar için takvimdeki en önemli tatil dönemlerinden biri Paskalya'dır.</p>

<p>Takvimlere baktığınızda 2026 yılı için <strong>3 Nisan</strong> tarihinin kırmızıyla işaretlendiğini görebilirsiniz. Ancak bu gün aslında o coşkulu ve renkli "Paskalya" kutlaması değil; Hristiyan dünyası için Paskalya hafta sonunun başlangıcı olan <strong>Kutsal Cuma (Karfreitag)</strong> günüdür. Peki, bu günün anlamı nedir ve Almanya'da (özellikle Mainz gibi şehirlerde) hayatı nasıl etkiler? Gelin bu uzun hafta sonunun detaylarına birlikte göz atalım.</p>

<h3>Kutsal Cuma (Karfreitag) Ne Anlama Geliyor?</h3>
<p>Hristiyan inancına göre Kutsal Cuma, İsa Mesih'in çarmıha gerildiği ve hayatını kaybettiği gündür. Bu nedenle, Pazar günü kutlanacak olan İsa'nın dirilişi (Paskalya) öncesinde tutulan bir <strong>yas, sessizlik ve oruç</strong> günüdür.</p>

<p>Almanya'da bu günün manevi ağırlığı, yasalarla da korunmaktadır. Kutsal Cuma, sıradan bir resmi tatil değil, <strong>"Sessiz Tatil" (Stiller Feiertag)</strong> statüsündedir.</p>

<h3>"Sessiz Tatil" Günlük Hayatı Nasıl Etkiler?</h3>
<p>Eğer 3 Nisan Cuma günü için eğlenceli planlar veya büyük bir alışveriş yapmayı düşünüyorsanız, planlarınızı gözden geçirmenizde fayda var:</p>
<ul>
  <li><strong>Dans Yasağı (Tanzverbot):</strong> Kutsal Cuma gününün en ilginç kurallarından biridir. Dini saygı çerçevesinde gece kulüplerinde, barlarda veya halka açık etkinliklerde dans etmek ve yüksek sesli müzik çalmak yasaktır. Çoğu eğlence mekanı perşembe gecesinden itibaren müziğin sesini kısar veya tamamen kapatır.</li>
  <li><strong>Kapalı Kepenkler:</strong> Almanya'nın genel kuralı burada da işler; tüm süpermarketler, mağazalar, okullar ve devlet daireleri kapalıdır. Sadece benzin istasyonları, tren garlarındaki küçük büfeler ve bazı fırınlar (sınırlı saatlerde) hizmet verir.</li>
</ul>

<h3>2026 Paskalya Hafta Sonu Takvimi ve Alışveriş Uyarısı!</h3>
<p>Almanya'da Paskalya dönemi toplam 4 günlük uzun bir hafta sonu tatili anlamına gelir. Evde yiyecek stoğunuzun bitmemesi için bu takvime dikkat etmeniz çok önemlidir:</p>
<ul>
  <li><strong>3 Nisan Cuma (Karfreitag):</strong> Resmi tatil. Her yer kapalı. Sokaklar oldukça sessiz.</li>
  <li><strong>4 Nisan Cumartesi (Karsamstag):</strong> Resmi tatil <em>değildir</em>. <strong>Dikkat!</strong> Bu gün, 4 günlük süreçte marketlerin ve mağazaların açık olduğu tek gündür. Bu nedenle marketlerde inanılmaz bir yoğunluk ve alışveriş telaşı yaşanır.</li>
  <li><strong>5 Nisan Pazar (Ostersonntag):</strong> Asıl <strong>Paskalya</strong> günüdür. Aileler bir araya gelir, geleneksel kahvaltılar yapılır. Çocuklar için bahçelerde veya parklarda saklanmış Paskalya yumurtaları ve çikolatalar aranır (Ostereiersuche).</li>
  <li><strong>6 Nisan Pazartesi (Ostermontag):</strong> Kutlamaların devam ettiği bu gün de resmi tatildir. Her yer yeniden kapalıdır.</li>
</ul>

<p>Özetle; 3 Nisan günü Almanya'da eğlencenin değil, içe dönüşün ve sakinliğin günüdür. Ancak bu sessizlik, pazar sabahı çocukların bahçelerde çikolata aradığı, ailelerin bir araya geldiği o renkli ve neşeli Paskalya coşkusuna hazırlık aşamasıdır.</p>
"""


def ekle(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')
    Stadt = apps.get_model('stadt', 'Stadt')
    User = apps.get_model('auth', 'User')

    mainz = Stadt.objects.filter(slug='mainz').first()
    yazar = User.objects.filter(is_superuser=True).first() or User.objects.first()

    if not yazar:
        return

    BlogYazisi.objects.get_or_create(
        slug='almanyada-paskalya-tatili-karfreitag-neden-sessiz',
        defaults=dict(
            baslik='Almanya\'da Paskalya Tatili: 3 Nisan Kutsal Cuma (Karfreitag) Neden Bu Kadar Sessiz?',
            icerik=ICERIK.strip(),
            ozet='Almanya\'da Paskalya tatili nasıl kutlanır? Karfreitag neden her yer kapalı? 2026 Paskalya takvimi ve alışveriş uyarısı.',
            kapak_resmi='https://images.unsplash.com/photo-1521334884684-d80222895322?w=1200&q=80',
            yazar=yazar,
            scope='stadt',
            stadt=mainz,
            yayinda=True,
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_helau_gercek_fotograf'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
