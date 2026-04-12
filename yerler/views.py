from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Case, When, IntegerField
from .models import Yer, YerFoto, ReklamPaketi, YerKategori


def _get_stadt(stadt_slug):
    if not stadt_slug:
        return None
    from stadt.models import Stadt
    return get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)


def _base_qs(stadt, eyalet_slug='rlp'):
    if stadt:
        return Yer.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug),
            aktif=True
        )
    return Yer.objects.filter(scope='eyalet', eyalet__slug=eyalet_slug, aktif=True)


# ── İşletmeler ───────────────────────────────────────────────────────────────

def isletmeler(request, eyalet_slug='rlp', stadt_slug=None):
    stadt = _get_stadt(stadt_slug)
    kategori = request.GET.get('kategori', '')

    paket_sira = Case(
        When(paket='pro', then=0),
        When(paket='plus', then=1),
        When(paket='temel', then=2),
        default=3,
        output_field=IntegerField(),
    )

    isletme_kategorileri = list(YerKategori.objects.filter(tur='isletme').order_by('sira', 'ad'))
    isletme_kodlari = [k.slug for k in isletme_kategorileri]
    base_qs = _base_qs(stadt, eyalet_slug).filter(
        tur='isletme', kategori__in=isletme_kodlari
    ).annotate(paket_sira=paket_sira).order_by('paket_sira', 'ad')

    kategoriler = {}
    for k in isletme_kategorileri:
        if kategori and k.slug != kategori:
            continue
        islt = base_qs.filter(kategori=k.slug)
        if islt.exists():
            kategoriler[k.slug] = {'ad': k.ad, 'yerler': islt}

    paketler = ReklamPaketi.objects.filter(aktif=True)

    return render(request, 'yerler/isletmeler.html', {
        'kategoriler':    kategoriler,
        'secili':         kategori,
        'tum_kategoriler': [(k.slug, k.ad) for k in isletme_kategorileri],
        'stadt':          stadt,
        'paketler':       paketler,
        'eyalet_slug':    eyalet_slug,
    })


# ── Detay (ortak) ────────────────────────────────────────────────────────────

def detay(request, pk, eyalet_slug='rlp', stadt_slug=None):
    stadt = _get_stadt(stadt_slug) if stadt_slug else None
    yer = get_object_or_404(Yer, pk=pk, aktif=True)
    fotolar = yer.fotolar.all()
    return render(request, 'yerler/detay.html', {
        'yer':         yer,
        'stadt':       stadt,
        'fotolar':     fotolar,
        'eyalet_slug': eyalet_slug,
    })


# ── Reklam Paketleri ─────────────────────────────────────────────────────────

def paketler(request, eyalet_slug='rlp'):
    paket_listesi = ReklamPaketi.objects.filter(aktif=True)
    iletisim_notu = paket_listesi.exclude(iletisim_notu='').values_list('iletisim_notu', flat=True).first()
    return render(request, 'yerler/paketler.html', {
        'paketler':      paket_listesi,
        'iletisim_notu': iletisim_notu,
        'eyalet_slug':   eyalet_slug,
    })
