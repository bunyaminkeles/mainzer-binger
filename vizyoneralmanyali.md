# Almanyalı Rehber - Vizyoner Geliştirme Promptları

Bu doküman, projenin temel prensiplerini (`almanyali.md`) bozmadan sistemi bir sonraki seviyeye taşıyacak özelliklerin geliştirilmesi için hazırlanmıştır. Claude veya Gemini gibi AI asistanlarına kopyala-yapıştır şeklinde verilerek kullanılabilir.

---

## 1. SEO Gözüyle: Programatik SEO ve Gelişmiş Şema

```text
Sen üst düzey bir Django ve SEO uzmanısın. Projemizin `almanyali.md` dokümantasyonuna harfiyen uymanı istiyorum (N+1 sorgu yasağı, select_related kullanımı).

GÖREV:
`yerler` uygulaması için Programatik SEO uyumlu bir liste görünümü (View) ve URL yapısı oluştur. 
Kullanıcı `/<eyalet_slug>/<stadt_slug>/isletmeler/<kategori_slug>/` adresine girdiğinde o şehirdeki o kategoriye ait aktif mekanları listelemeliyiz.

GEREKSİNİMLER:
1. `urls.py` (stadt_urls.py) içine ilgili route'u ekle (`isletmeler/<slug:kategori_slug>/`).
2. `views.py` içinde `YerListByCategoryView` oluştur. DİKKAT: `Yer.kategori` alanı bir FK değil, CharField'dır (slug tutar). Bu yüzden `YerKategori` nesnesini URL'den gelen slug ile ayrı bir sorgu (`get_object_or_404`) olarak çekmeli, ardından `Yer.objects.filter(kategori=kategori.slug, stadt=..., aktif=True).select_related('stadt')` şeklinde filtrelemelisin. Asla N+1 sorgu yapma.
3. Bu sayfa için Google'ın anlayacağı `<script type="application/ld+json">` `ItemList` ve listelenen yerler için `LocalBusiness` Schema.org verisini üreten bir bağlam (context) ekle.
4. Şablon kodunu (HTML) yazarken Vanilla JS ve Bootstrap 5 kullan. Asla Tailwind veya React kullanma.
```

## 2. CEO Gözüyle: Lokal Uzmanlar Analitik Dashboard

```text
Sen bir B2B SaaS ürün yöneticisi ve Django Backend geliştiricisisin. `almanyali.md` kurallarına sadık kalarak `businesses` (Lokal Uzmanlar) modülüne bir analitik kokpiti ekleyeceğiz.

GÖREV:
İşletme sahiplerinin profillerinin ne kadar etkileşim aldığını görebileceği bir Dashboard oluştur.

GEREKSİNİMLER:
1. `BusinessAnalytics` modelini kullanarak, giriş yapmış kullanıcının sahip olduğu (`is_published=True`) işletmenin son 30 günlük "Görüntülenme" ve "WhatsApp Tıklama" verilerini toplayan bir Django View yaz.
2. Frontend'de bu veriyi göstermek için basit bir Vanilla JS tabanlı grafik veya Bootstrap 5 sınıflarını (`--primary`, `--accent` tokenları ile) kullanarak estetik metrik kartları (Widget) tasarla. Dışarıdan ağır bir chart kütüphanesi yüklemek yerine, CSS Grid (`.tas-grid`) ve modern HTML/CSS kullan.
3. API tarafı için `api/` klasörü altında bu veriyi JSON dönen bir endpoint yaz (ileride mobil uygulamada kullanılmak üzere).
4. `almanyali.md` kuralı gereği, Modülün aktif olup olmadığını `GlobalSetting.is_business_module_active` üzerinden kontrol etmeyi unutma!
```

## 3. Yatırımcı Gözüyle: SaaS Büyüme Raporu Komutu

```text
Sen bir Veri Mühendisi ve Django uzmanısın. Yatırımcılara sunacağımız metrikleri hesaplamak için bir arka plan aracı yazacağız.

GÖREV:
`businesses` app'i içinde yatırımcı sunumları için temel SaaS metriklerini (MRR, Aktif İşletme Sayısı, Churn Oranı) hesaplayan bir Django Management Command yaz.

GEREKSİNİMLER:
1. Komut `python manage.py metrik_raporu` şeklinde çalışmalı.
2. Sistemdeki aktif (`is_published=True` ve `end_date` süresi dolmamış) `LocalBusiness` kayıtlarını ve `SubscriptionPlan` fiyatlarını baz alarak toplam MRR'ı (Aylık Gelir) hesapla.
3. Son 30 günde biten ve yenilenmeyen aboneliklerden Churn (Kayıp) oranını hesapla.
4. Çıktıyı konsola estetik ve okunabilir bir formatta (Terminal tabloları veya renkli text) bas.
5. Veritabanını yormamak için `aggregate`, `Sum`, `Count` gibi Django ORM fonksiyonlarını verimli kullan, Python seviyesinde loop (N+1) yapma.
```

## 4. Kullanıcı Olarak: İlk 90 Gün İnteraktif Yol Haritası

```text
Sen bir UX/UI Geliştiricisi ve Frontend mimarısın. Tasarım felsefemiz olan "Apple/Stripe sadeliğinde, sıfır bilişsel yük" kuralına ve Vanilla JS/Bootstrap 5 mimarisine (`almanyali.md`) harfiyen uyacaksın.

GÖREV:
Kullanıcı profilinde (Kokpit) yer alacak "İlk 90 Gün Yol Haritası" (Onboarding Checklist) bileşenini tasarla ve kodla.

GEREKSİNİMLER:
1. `accounts` app'indeki Profil modeline, tamamlanan görevleri tutacak basit bir JSONField veya ArrayField ekle (örn: `completed_tasks`).
2. HTML şablonunda: Anmeldung, Banka Hesabı, Vergi Numarası, Sigorta gibi 4-5 adımlık bir interaktif checklist yap.
3. CSS: `.kart` ve `.card-hover` sınıflarımızı kullanarak görevleri liste halinde göster.
4. JS: Kullanıcı bir görevi işaretlediğinde (checkbox), sayfa YENİLENMEDEN (No-Reload kuralı) Fetch API ile backend'e istek at, başarılı dönerse checkbox'ı yeşil (`--accent`) yap. Optimistic UI yaklaşımı kullan. jQuery, React veya Vue KESİNLİKLE YASAKTIR.
```

## 5. Backend Developer Olarak: Celery Geçişi ve Testler

```text
Sen çok tecrübeli bir Python/Django Backend Mimarısın. Projenin `almanyali.md` dosyasına hakimsin.

GÖREV:
Mevcut durumda `django-crontab` ile çalışan `duyuru_gonder` ve `bulten_gonder` komutlarını Celery ve Redis altyapısına taşıyacak temel mimariyi kur. Ayrıca kritik sistemler için test yaz.

GEREKSİNİMLER:
1. `settings.py` için gerekli Celery ve Redis konfigürasyonlarını yaz.
2. `rehber/tasks.py` oluştur ve toplu mail gönderim mantığını (`django-anymail` SMTP kullanarak) buraya asenkron bir task (shared_task) olarak taşı.
3. Sistemin sağlamlığını kanıtlamak için `pytest-django` kullanarak `businesses` app'indeki abonelik paketinin aktif olup olmadığını kontrol eden (`LocalBusiness.is_currently_active`) property için Unit Test yaz.
4. Testlerde asla production veritabanına dokunulmamalı, mock nesneler kullanılmalıdır.
```

## 6. UI Developer Olarak: Tekrar Kullanılabilir Component

```text
Sen Vanilla JS ustası bir Frontend mimarısın. Projemizde framework yasağı (`almanyali.md`) olduğu için temiz bir yapı kurmalıyız.

GÖREV:
Sistemdeki tüm AJAX form gönderimlerini ve bildirimlerini (Toast/Flash) standartlaştıran yeniden kullanılabilir bir Vanilla JS class'ı yaz.

GEREKSİNİMLER:
1. `static/js/components/FetchForm.js` adında bir sınıf oluştur.
2. Bu sınıf herhangi bir `<form data-fetch="true">` etiketini yakalamalı, preventDefault yapmalı ve veriyi Fetch API ile göndermeli.
3. Bekleme esnasında butonun içine Bootstrap 5 Spinner koymalı (buton state yönetimi).
4. İstek başarılıysa formun içeriğini temizlemeli ve ekrana (varsa Bootstrap Toast kullanarak) "Başarılı" mesajı çıkarmalı.
5. Hata durumlarında Django form hatalarını (JSON dönen) yakalayıp ilgili inputların altında kırmızı renkte göstermeli.
6. Hiçbir şekilde bağımlılık (npm, jQuery vb.) kullanılmamalıdır.
```

## 7. Almanya'ya Yeni Gelmiş Biri Olarak: Bürokratik Çeviri Aracı

```text
Sen hem bir AI entegrasyon uzmanı hem de Almanya bürokrasisini iyi bilen birisin. `almanyali.md` kural setini unutmuyorsun.

GÖREV:
"Resmi Evrak Çevirmeni" adında küçük bir interaktif araç (Wizard) oluşturacağız.

GEREKSİNİMLER:
1. `core` veya `rehber` app'i altında `BurokrasiSozlugu` adında bir model oluştur (Almanca terim, Türkçe Karşılık, Ne Yapmalı). Örn: "Frist" -> "Son Teslim Tarihi" -> "Bu tarihe kadar cevap vermelisin".
2. Kullanıcının bir Almanca cümleyi yapıştırdığı bir arama/analiz formu yap (Bootstrap 5 ile şık bir tasarım, `.anasayfa-panel` içinde).
3. Backend tarafında (Vanilla JS Fetch ile bağlanacak), kullanıcının girdiği metni analiz edip veritabanındaki kritik bürokrasi kelimelerini (`Widerspruch`, `Nachweis` vb.) bulan ve bu kelimelerin anlamlarını + eylem çağrılarını JSON dönen bir View yaz.
4. Sonucu ekranda anında (sayfa yenilemeden) göster.
```