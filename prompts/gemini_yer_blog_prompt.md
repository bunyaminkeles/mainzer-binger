# Gezilecek Yer Blog Yazısı — Prompt Şablonu

Aşağıdaki formatta bir JSON çıktısı üret. Başka hiçbir şey yazma, sadece JSON.

---

## Kullanım

Şehir: **[ŞEHİR ADI]**
Şehir slug: **[şehir-slug]** (örnek: berlin, hamburg, münchen)

Yerler listesi:
1. [Yer Adı] — Resim: [URL] — Kaynak: [URL]
2. [Yer Adı] — Resim: [URL] — Kaynak: [URL]

---

## Gemini'ye Verilecek Prompt

```
Aşağıdaki gezilecek yerler için Türkçe blog içerikleri yaz ve JSON formatında çıktı ver.

Şehir: {ŞEHİR}
Şehir slug: {SLUG}

Yerler:
{YER_LİSTESİ}

Kurallar:
- Her yer için "icerik" alanı HTML formatında olmalı (p, h3, h4, ul, li, strong, em, hr tagları kullan)
- "icerik" en az 400 kelime olmalı
- "aciklama" max 200 karakter, SEO dostu özet cümle
- "kategori" değeri her zaman: gezi
- "adres" alanına şehirdeki semti veya meydanı yaz
- Çıktı sadece geçerli JSON olsun, başka açıklama ekleme
- Her yerin "id" alanını boş bırak (null yaz)

Çıktı formatı:
{
  "stadt_slug": "{SLUG}",
  "yerler": [
    {
      "id": null,
      "ad": "Yer Adı",
      "kategori": "gezi",
      "adres": "Adres, Şehir",
      "aciklama": "Kısa SEO açıklama...",
      "kapak_resmi": "BURAYA_RESİM_URL_GEL",
      "wikipedia_url": "BURAYA_KAYNAK_URL_GEL",
      "icerik": "<p>İçerik...</p>"
    }
  ]
}
```

---

## Sunucuda Çalıştırma

1. JSON çıktısını `veri.json` olarak kaydet
2. Sunucuya kopyala (scp veya nano ile)
3. Çalıştır:

```bash
python manage.py yer_icerik_yukle /tmp/veri.json
```

4. Temizle:

```bash
rm /tmp/veri.json
```

---

## Mevcut Kayıtları Güncellemek İçin

Eğer DB'de zaten kayıt varsa `"id"` alanına DB id'sini yaz, komut günceller:

```json
{ "id": 117, "ad": "Berliner Fernsehturm", ... }
```
