from django.db import migrations

YAZILAR = [
    {
        'slug': 'almanya-banka-hesabi-acma',
        'baslik': "Almanya'da Banka Hesabı Açma Rehberi",
        'ozet': "Almanya'da maaş, kira ve günlük harcamalar için banka hesabı nasıl açılır? Gerekli belgeler ve en iyi banka seçenekleri.",
        'icerik': "<p>Bu sayfa yapım aşamasındadır. Yakında Almanya'da banka hesabı açma süreciyle ilgili detaylı bilgiler eklenecektir.</p>",
    },
    {
        'slug': 'almanya-steuer-id-nedir',
        'baslik': "Almanya'da Vergi Kimlik Numarası (Steuer-ID) Nedir ve Nasıl Alınır?",
        'ozet': "Steueridentifikationsnummer (Vergi ID) neden önemlidir, nasıl alınır ve nerede kullanılır? Almanya'daki vergi sistemine ilk adım.",
        'icerik': "<p>Bu sayfa yapım aşamasındadır. Yakında Almanya'da Vergi Kimlik Numarası (Steuer-ID) alma süreciyle ilgili detaylı bilgiler eklenecektir.</p>",
    },
    {
        'slug': 'almanya-saglik-sigortasi-rehberi',
        'baslik': "Almanya Sağlık Sigortası (Krankenversicherung) Rehberi",
        'ozet': "Almanya'da yasal sağlık sigortası (GKV) ve özel sağlık sigortası (PKV) arasındaki farklar nelerdir? Nasıl başvuru yapılır?",
        'icerik': "<p>Bu sayfa yapım aşamasındadır. Yakında Almanya'da sağlık sigortası sistemi ve başvuru süreciyle ilgili detaylı bilgiler eklenecektir.</p>",
    },
]


def ekle(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')
    User = apps.get_model('auth', 'User')

    yazar = User.objects.filter(is_superuser=True).first() or User.objects.first()

    if not yazar:
        return

    for yazi_data in YAZILAR:
        BlogYazisi.objects.get_or_create(
            slug=yazi_data['slug'],
            defaults=dict(
                baslik=yazi_data['baslik'],
                icerik=yazi_data['icerik'],
                ozet=yazi_data['ozet'],
                yazar=yazar,
                scope='genel',
                yayinda=True,
            ),
        )

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_helau_karneval_yazisi'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]