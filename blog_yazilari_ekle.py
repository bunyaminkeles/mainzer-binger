"""
Mainz'deki görülmeye değer 5 yer için blog yazısı ekler.
Çalıştırmak için: python manage.py shell < blog_yazilari_ekle.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import BlogYazisi

# Yazar: ilk superuser veya ilk kullanıcı
try:
    yazar = User.objects.filter(is_superuser=True).first() or User.objects.first()
    if not yazar:
        yazar = User.objects.create_superuser('mainzer_admin', 'admin@mainzer-binger.de', 'MainzerBinger2024!')
        print(f"Yeni admin kullanıcı oluşturuldu: {yazar.username}")
    else:
        print(f"Yazar: {yazar.username}")
except Exception as e:
    print(f"Kullanıcı hatası: {e}")
    exit()

yazılar = [
    {
        "baslik": "Mainz Dom: Bin Yıllık Tarihin Kalbi",
        "slug": "mainz-dom-bin-yillik-tarihin-kalbi",
        "kapak_resmi": "https://images.unsplash.com/photo-1596484552834-6a58f850e0a1?w=1200&q=80",
        "ozet": "Mainz'in simgesi, Kutsal Roma İmparatorluğu'nun taç giyme kilisesi: Mainzer Dom'u keşfediyoruz.",
        "icerik": """
<p><strong>Mainz Katedrali</strong> (Almanca: <em>Hohe Dom zu Mainz</em>), şehrin tam kalbinde yükselen ve binin üzerinde yıllık tarihe sahip muhteşem bir Roma-Germen katedralidir. Mainz'e yeni gelenlerin mutlaka ziyaret etmesi gereken bu yapı, şehrin en önemli simgesi olma özelliğini bugün de korumaktadır.</p>

<img src="https://images.unsplash.com/photo-1467818693588-be7a5a7e4c14?w=1000&q=80" alt="Mainz Dom iç mekan" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Tarihi</h2>
<p>İlk katedrali 975 yılında tamamlanan yapı, yüzyıllar içinde pek çok yangın geçirmiş, yeniden inşa edilmiş ve genişletilmiştir. Bugün ayakta duran katedrali, büyük ölçüde 11–13. yüzyıllara tarihlenmektedir. Otuz Yıl Savaşları ve II. Dünya Savaşı'nda hasar gören yapı, titizlikle restore edilerek orijinal görünümüne kavuşturulmuştur.</p>

<div class="info-box">
  <strong>📍 Adres:</strong> Domstraße 3, 55116 Mainz<br>
  <strong>🕐 Ziyaret Saatleri:</strong> Pzt–Cu 09:00–18:30 | Cts 09:00–18:00 | Paz 12:30–18:00<br>
  <strong>💶 Giriş:</strong> Ücretsiz (Müze için ücret alınmaktadır)<br>
  <strong>🚇 Ulaşım:</strong> Tramvay 50/51/52/53 – Dom/Römerpassage durağı
</div>

<h2>Mimari Özellikler</h2>
<p>Dom, Geç Roma ve Erken Gotik mimarinin eşsiz bir sentezini sunar. Yapının en dikkat çekici özellikleri arasında altı kulesi, kırmızı Mainz kumtaşından örülmüş dış cephesi ve muhteşem bronz kapıları sayılabilir. İç mekânda ise asırlık mezar taşları, görkemli sütunlar ve renkli vitray pencereler ziyaretçileri büyüler.</p>

<img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1000&q=80" alt="Katedrale yakın görünüm" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Türkçe Konuşan Ziyaretçiler İçin İpuçları</h2>
<p>Katedrali ziyaret etmek için önceden rezervasyon gerekmez; ancak dini törenlerin yoğun olduğu Pazar sabahları ve özel kutlamalarda kilise turistlere kapalı olabilir. Dom'un hemen yanındaki <strong>Dommuseum</strong>'u da kesinlikle görün — burada yüzyıllık dini eserler ve sanat yapıtları sergilenmektedir.</p>

<p>Kışın bile ziyaret edilebilir olan katedral, Noel Pazarı döneminde (Advent zamanı) çevresindeki meydanın büyüleyici atmosferiyle birleşince tam anlamıyla masalsı bir görünüm kazanır.</p>
""",
    },
    {
        "baslik": "Gutenberg Müzesi: Matbaanın Doğduğu Yer",
        "slug": "gutenberg-muzesi-matbaanin-dogdugu-yer",
        "kapak_resmi": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=1200&q=80",
        "ozet": "Johannes Gutenberg'in matbaayı icat ettiği şehirde, ona adanmış eşsiz müzeyi ziyaret ediyoruz.",
        "icerik": """
<p>Matbaanın mucidi <strong>Johannes Gutenberg</strong>'in doğduğu ve ölümsüz keşfini gerçekleştirdiği şehir olan Mainz'de, ona adanmış dünya çapında ünlü bir müze bulunmaktadır: <strong>Gutenberg Müzesi</strong>. İnsanlığın bilgi tarihini değiştiren hareketli hurufat baskı tekniğinin hikâyesini anlatan bu müze, her yaştan ziyaretçiyi büyülemeye devam etmektedir.</p>

<img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?w=1000&q=80" alt="Eski kitaplar ve matbaa" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Müzenin Kalbi: Gutenberg İncili</h2>
<p>Müzenin en değerli eseri şüphesiz <strong>Gutenberg İncili</strong>'dir (42 Satırlık İncil olarak da bilinir). Dünyanın dört bir yanındaki 49 kopyasından sadece ikisi tam olarak günümüze ulaşmış; bu kopyalardan biri Gutenberg Müzesi'nde sergilenmektedir. Yaklaşık 1455 yılında basılan bu incil, hareketli metal hurufatla basılan ilk büyük kitaplar arasında yer almaktadır.</p>

<div class="info-box">
  <strong>📍 Adres:</strong> Liebfrauenplatz 5, 55116 Mainz<br>
  <strong>🕐 Ziyaret Saatleri:</strong> Salı–Cmt 09:00–17:00 | Pazar 11:00–17:00 | Pazartesi kapalı<br>
  <strong>💶 Giriş:</strong> Yetişkin 5 € | Öğrenci/65+ 3 € | 18 yaş altı ücretsiz<br>
  <strong>🚇 Ulaşım:</strong> Dom/Römerpassage durağı – yürüme mesafesinde
</div>

<h2>Matbaacılığı Bizzat Deneyin</h2>
<p>Müzede yalnızca sergilere bakmakla kalmayacaksınız — rehberli turlarda <strong>tarihî baskı makinesini çalışırken</strong> izleyebilir, hatta kendi baskınızı yapabilirsiniz! Atölye çalışmaları özellikle çocuklar ve gençler için harika bir deneyim sunmaktadır.</p>

<img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000&q=80" alt="Tarihî baskı teknikleri" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Neden Mutlaka Görülmeli?</h2>
<p>Gutenberg'in icadı olmasa, kitapların bu denli yaygınlaşması, Reformasyon'un yayılması, bilimin gelişmesi ve insanlığın bugünkü bilgi birikimini oluşturması çok daha uzun sürerdi. Müze, bu devasa etkiyi son derece etkileyici ve eğlenceli bir biçimde aktarmaktadır. Mainz'e geldiyseniz bu müzeyi atlamak büyük bir eksiklik olur.</p>

<p>💡 <strong>İpucu:</strong> Her yıl Haziran ayında düzenlenen <em>Johannisnacht</em> (Gutenberg Festivali) sırasında müze özel etkinlikler düzenlemekte, sokaklar canlı müzik ve sanat performanslarıyla dolmaktadır. Bu tarihlere denk gelirseniz şansınızı iyi kullanın!</p>
""",
    },
    {
        "baslik": "Ren Nehri Yürüyüş Yolu: Mainz'in Mavi Şeridi",
        "slug": "ren-nehri-yuruyus-yolu-mainzin-mavi-seridi",
        "kapak_resmi": "https://images.unsplash.com/photo-1564961704930-c6e9b8b3a513?w=1200&q=80",
        "ozet": "Mainz'in Ren Nehri kıyısındaki yürüyüş yolunda bir gün geçirin, Theodor-Heuss Köprüsü'nden akşam manzarasına hayran kalın.",
        "icerik": """
<p><strong>Ren Nehri</strong> (Almanca: Rhein), Avrupa'nın en önemli nehirlerinden biri olarak Mainz'in batı sınırını çizmekte ve şehre eşsiz bir atmosfer katmaktadır. Mainz'e yerleşen ya da tatile gelenler için Ren kıyısı yürüyüş yolu, saatlerce vakit geçirilebilecek güzel bir rotadır.</p>

<img src="https://images.unsplash.com/photo-1600715514001-1ebe59cef7db?w=1000&q=80" alt="Ren nehri manzarası" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Rheinufer Promenadı</h2>
<p>Mainz merkezdeki <strong>Rheinufer</strong> (Ren Kıyısı) promenadı, özellikle ilkbahar ve yaz aylarında yerel halkın sevdiği buluşma noktalarından biridir. Uzun yürüyüş yolları, bisiklet parkurları ve oturma alanlarıyla donatılmış kıyı şeridi, aileler, sporcular ve sadece manzara keyfetmek isteyenler için mükemmeldir.</p>

<div class="info-box">
  <strong>📍 Başlangıç Noktası:</strong> Theodor-Heuss-Brücke yakını (Rheingoldhalle önü)<br>
  <strong>🚶 Yürüyüş Süresi:</strong> Güneye doğru yaklaşık 3–5 km'lik kolay yürüyüş<br>
  <strong>🚲 Bisiklet:</strong> Ren kıyısı bisiklet yolu tüm güzergah boyunca devam eder<br>
  <strong>🌅 En İyi Zaman:</strong> Günbatımı saatleri — nehirdeki yansıma büyüleyici
</div>

<h2>Kıyıdaki Duraklar</h2>
<p>Yürüyüş rotasında mutlaka uğranması gereken yerler:</p>
<ul>
  <li><strong>Fischtorplatz:</strong> Ren kıyısındaki bu meydanda birçok balık restoranı ve kafeler bulunmaktadır.</li>
  <li><strong>Winterhafen:</strong> Eski liman bölgesi günümüzde dönüştürülerek modern mimarisiyle öne çıkan bir yaşam alanına kavuşmuştur.</li>
  <li><strong>Mainz-Kastel Köprüsü:</strong> Biraz daha uzağa uzananlara Hessen eyaletine geçişi sağlayan köprüden harika fotoğraflar çekme fırsatı sunar.</li>
</ul>

<img src="https://images.unsplash.com/photo-1559521783-1d1599583485?w=1000&q=80" alt="Ren nehri gün batımı" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Türkçe Konuşanlar İçin Pratik Bilgiler</h2>
<p>Kıyı şeridinde Türk veya uluslararası mutfak sunan birçok restoran bulunmaktadır. Özellikle yaz aylarında nehir üzerinde <strong>Ren gemi turları</strong> düzenlenmektedir; bu turlar için Rhine cruise operatörlerinin web sitelerini inceleyebilirsiniz.</p>

<p>Bir piknik sepeti hazırlayarak kıyıda güneşli bir öğleden sonra geçirmek de harika bir seçenektir. Yakınlardaki <em>Wochenmarkt</em>'tan (haftalık pazar) taze ürünler alıp nehir kenarında mola verebilirsiniz.</p>
""",
    },
    {
        "baslik": "Kurfürstliches Schloss: Barok İhtişamın Gözdesi",
        "slug": "kurfurstliches-schloss-barok-ihtisamin-gozdesi",
        "kapak_resmi": "https://images.unsplash.com/photo-1533050487297-09b450131914?w=1200&q=80",
        "ozet": "Mainz'in en görkemli yapılarından Kurfürstliches Schloss — Seçici Kral Sarayı'nı keşfediyoruz.",
        "icerik": """
<p>Mainz'in Ren Nehri kıyısında yükselen <strong>Kurfürstliches Schloss</strong> (Seçici Kral Sarayı), Almanya'nın en güzel barok saraylarından biri olarak kabul edilmektedir. 18. yüzyılda inşa edilen bu görkemli yapı, bugün Mainz Üniversitesi'ne bağlı çeşitli birimler ve müzeler için ev sahipliği yapmaktadır.</p>

<img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=1000&q=80" alt="Barok saray mimarisi" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Tarihi ve Önemi</h2>
<p>Saray, Mainz Seçici Kontu (Kurfürst) ve Başpiskoposu <strong>Lothar Franz von Schönborn</strong> döneminde 1627 yılında başlayan ve uzun yıllar süren bir inşaat sürecinin ürünüdür. Fransız Devrim Savaşları sırasında büyük hasar gören yapı, 19. yüzyılda restore edilmiştir. Sarının ferah tonlarındaki dış cephesiyle Ren kıyısında son derece etkileyici bir görünüm sunmaktadır.</p>

<div class="info-box">
  <strong>📍 Adres:</strong> Peter-Altmeier-Ufer 1, 55116 Mainz<br>
  <strong>🌳 Bahçe:</strong> Saray bahçesi halka açık ve ücretsiz<br>
  <strong>🚇 Ulaşım:</strong> Rheingoldhalle/Rathaus tram durağı – 5 dk yürüme<br>
  <strong>📸 Fotoğraf:</strong> Nehir tarafından çekilen akşam fotoğrafları muhteşem çıkar!
</div>

<h2>Saray Bahçesinde Vakit Geçirin</h2>
<p>Sarayın güney cephesindeki <strong>barok bahçe</strong>, özellikle ilkbahar ve yaz aylarında çiçekleriyle görsel bir şölen sunar. Bahçede oturup Ren manzarasına bakmak ve Dom'un kuleleriyle saray binasının bir arada göründüğü silueti fotoğraflamak için harika bir yer.</p>

<img src="https://images.unsplash.com/photo-1543631936-4019110ec8b5?w=1000&q=80" alt="Barok bahçe" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Ziyaret İpuçları</h2>
<p>Sarayın içinde yer alan <strong>Landesmuseum Mainz</strong>'i de ziyaret etmeyi unutmayın. Rhineland-Palatinate eyaletinin en kapsamlı sanat ve tarih koleksiyonuna sahip bu müze, Mainz'in antik çağdan günümüze uzanan tarihini eserler eşliğinde aktarmaktadır.</p>

<p>Saray önündeki <strong>Rheinufer</strong> yürüyüş yolunda akşam molası verip dondurma yemek ise Mainz'lilerin en sevdiği geleneklerden biri. Yaz akşamları burada adeta küçük bir şenlik havası oluşmaktadır.</p>
""",
    },
    {
        "baslik": "St. Stephan Kilisesi: Chagall'ın Mavi Işığı",
        "slug": "st-stephan-kilisesi-chagallin-mavi-isigi",
        "kapak_resmi": "https://images.unsplash.com/photo-1548266652-99cf27701ced?w=1200&q=80",
        "ozet": "Marc Chagall'ın yarattığı efsanevi mavi vitray pencerelerle ışıl ışıl parlayan St. Stephan Kilisesi, Mainz'in saklı hazinesidir.",
        "icerik": """
<p>Mainz'de pek çok güzel kilise bulunsa da <strong>St. Stephan Kilisesi</strong> (Alman-Fransız dostluğunun ve barışın sembolü olarak da anılır), dünyaca ünlü sanatçı <strong>Marc Chagall</strong>'ın eserleriyle ayrı bir yere sahiptir. Kiliseye girer girmez sizi saran o eşsiz mavi ışık, bir daha asla unutamayacağınız türden bir deneyim sunmaktadır.</p>

<img src="https://images.unsplash.com/photo-1558618047-f4e9c01671b2?w=1000&q=80" alt="Vitray pencere ışığı" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Chagall Pencereleri</h2>
<p>Marc Chagall, 1978 yılında (93 yaşındayken!) <strong>9 büyük vitray pencere</strong> tasarlamış ve bu pencereler 1978–1985 yılları arasında kiliseye yerleştirilmiştir. Güneşin yaptığı açıya göre rengi değişen bu pencerelerdeki yoğun mavi ton, içeriye masalsı bir ışık oyunu yansıtmaktadır. Chagall bu eserleri, Nazi zulmünde hayatını kaybeden Yahudi ve Hristiyan kurbanların anısına ve Alman-Fransız barışının simgesi olarak yaratmıştır.</p>

<div class="info-box">
  <strong>📍 Adres:</strong> Kleine Weißgasse 12, 55116 Mainz<br>
  <strong>🕐 Ziyaret Saatleri:</strong> Pzt–Cu 10:00–12:00, 14:00–17:00 | Cts 12:00–17:00 | Paz 12:00–17:00<br>
  <strong>💶 Giriş:</strong> Ücretsiz (bağış hoş görülür)<br>
  <strong>🚶 Ulaşım:</strong> Dom'dan 10 dakika yürüme mesafesinde, yokuş yukarı
</div>

<h2>Sabah Ziyareti Tavsiyesi</h2>
<p>Chagall pencerelerini en iyi koşullarda görmek için <strong>güneşli bir sabah</strong> tercih edin. Sabah güneşinin doğudan vurduğu saatlerde pencereler adeta yanar gibi parlar. Öğleden sonra gün batımına yakın saatlerde ise farklı bir atmosfer hâkim olur.</p>

<img src="https://images.unsplash.com/photo-1580274455191-1c62238fa333?w=1000&q=80" alt="Kilise iç mekânı" style="max-width:100%;border-radius:10px;margin:1.5rem 0;box-shadow:0 4px 16px rgba(0,0,0,0.1);">

<h2>Kilise ve Çevresi</h2>
<p>St. Stephan, Mainz'in yukarı kesimindeki <strong>Stephansplatz</strong> meydanında yer almaktadır. Katedrale kıyasla çok daha sessiz ve sakin bir ortamda ziyaret edebildiğiniz bu kilise, şehrin gürültüsünden uzaklaşmak isteyenler için de mükemmel bir duraktır. Kilise çıkışında yakındaki Weinstube'lerden birinde Rheinhessen şarabı eşliğinde öğle yemeği yiyebilirsiniz.</p>

<p>Mainz'deki Türk topluluğunun büyük bir kısmı bu kiliseden habersiz olduğu için <em>saklı hazine</em> olarak nitelendiriliyor. Ama bir kez görünce neden bu kadar meşhur olduğunu çok iyi anlayacaksınız. Chagall'ın mavi dünyasına dalmak gerçekten unutulmaz bir an.</p>
""",
    },
]

eklendi = 0
guncellendi = 0

for veri in yazılar:
    yazi, created = BlogYazisi.objects.get_or_create(
        slug=veri["slug"],
        defaults={
            "baslik": veri["baslik"],
            "kapak_resmi": veri["kapak_resmi"],
            "icerik": veri["icerik"].strip(),
            "ozet": veri["ozet"],
            "yayinda": True,
            "yazar": yazar,
        }
    )
    if created:
        eklendi += 1
        print(f"  ✓ Eklendi: {yazi.baslik}")
    else:
        # Güncelle (içerik değişmiş olabilir)
        yazi.baslik = veri["baslik"]
        yazi.kapak_resmi = veri["kapak_resmi"]
        yazi.icerik = veri["icerik"].strip()
        yazi.ozet = veri["ozet"]
        yazi.yayinda = True
        yazi.save()
        guncellendi += 1
        print(f"  ↻ Güncellendi: {yazi.baslik}")

print(f"\n✅ Tamamlandı: {eklendi} yeni, {guncellendi} güncellendi.")
