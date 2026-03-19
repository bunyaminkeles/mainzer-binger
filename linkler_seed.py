"""
Temel linkleri ve rehber kaynaklarını yükler.
Kullanım: python linkler_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from linkler.models import OnemliLink
from rehber.models import Kaynak

# ── Önemli Linkler ───────────────────────────────────────────────
LINKLER = [
    dict(ad='Mainz Jobcenter', url='https://www.jobcenter-mainz.de/',
         kategori='is', sira=1,
         aciklama='İşsizlik yardımı, iş arama desteği ve sosyal yardım başvuruları.'),
    dict(ad='Bundesagentur für Arbeit', url='https://web.arbeitsagentur.de/',
         kategori='is', sira=2,
         aciklama='Federal İş Kurumu — ALG I, iş ilanları ve kariyer danışmanlığı.'),
    dict(ad='T.C. Mainz Başkonsolosluğu', url='https://mainz-bk.mfa.gov.tr/Mission',
         kategori='resmi', sira=1,
         aciklama='Pasaport, vize, nüfus işlemleri ve konsolosluk hizmetleri.'),
    dict(ad='Mainz Şehir Portalı', url='https://www.mainz.de/',
         kategori='resmi', sira=2,
         aciklama='Mainz Belediyesi resmi sitesi — haberler, hizmetler, vatandaş işlemleri.'),
]

# ── Rehber Kaynakları ────────────────────────────────────────────
REHBER = [
    dict(baslik='Mainz Jobcenter', tip='link', url='https://www.jobcenter-mainz.de/',
         kategori='is', icon='bi-briefcase', sira=1, yayinda=True,
         ozet='İşsizlik yardımı ve iş arama desteği için başvuru noktası.'),
    dict(baslik='Bundesagentur für Arbeit (İş Kurumu)', tip='link',
         url='https://web.arbeitsagentur.de/',
         kategori='is', icon='bi-building', sira=2, yayinda=True,
         ozet='ALG I, iş ilanları ve kariyer danışmanlığı için Federal İş Kurumu.'),
    dict(baslik='T.C. Mainz Başkonsolosluğu', tip='link',
         url='https://mainz-bk.mfa.gov.tr/Mission',
         kategori='resmi', icon='bi-flag', sira=1, yayinda=True,
         ozet='Pasaport, vize, nüfus işlemleri ve tüm konsolosluk hizmetleri.'),
    dict(baslik='Mainz Belediyesi (mainz.de)', tip='link', url='https://www.mainz.de/',
         kategori='resmi', icon='bi-building-fill', sira=2, yayinda=True,
         ozet='Mainz şehir portalı — belediye hizmetleri, haberler ve duyurular.'),
]

eklendi = 0
for d in LINKLER:
    _, created = OnemliLink.objects.get_or_create(url=d['url'], defaults=d)
    if created:
        eklendi += 1
        print(f'  ✓ Link: {d["ad"]}')

for d in REHBER:
    _, created = Kaynak.objects.get_or_create(url=d['url'], defaults=d)
    if created:
        eklendi += 1
        print(f'  ✓ Rehber: {d["baslik"]}')

print(f'✅ {eklendi} yeni kayıt eklendi.')
