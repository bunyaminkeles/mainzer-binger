from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Case, When, IntegerField
from .models import Yer, YerFoto, ReklamPaketi, YER_KATEGORI


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategori = request.GET.get('kategori', '')

    paket_sira = Case(
        When(paket='one_cikan', then=0),
        When(paket='standart', then=1),
        default=2,
        output_field=IntegerField(),
    )

    if stadt:
        base_qs = Yer.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            aktif=True
        )
    else:
        base_qs = Yer.objects.filter(aktif=True)

    base_qs = base_qs.annotate(paket_sira=paket_sira).order_by('paket_sira', 'ad')

    kategoriler = {}
    for k, v in YER_KATEGORI:
        if kategori and k != kategori:
            continue
        yerler = base_qs.filter(kategori=k)
        if yerler.exists():
            kategoriler[k] = {'ad': v, 'yerler': yerler}

    return render(request, 'yerler/liste.html', {
        'kategoriler': kategoriler,
        'secili': kategori,
        'tum_kategoriler': YER_KATEGORI,
        'stadt': stadt,
    })


def detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    yer = get_object_or_404(Yer, pk=pk, aktif=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    fotolar = yer.fotolar.all()
    return render(request, 'yerler/detay.html', {
        'yer': yer,
        'stadt': stadt,
        'fotolar': fotolar,
    })


def paketler(request):
    paket_listesi = ReklamPaketi.objects.filter(aktif=True)
    iletisim_notu = paket_listesi.exclude(iletisim_notu='').values_list('iletisim_notu', flat=True).first()
    return render(request, 'yerler/paketler.html', {
        'paketler': paket_listesi,
        'iletisim_notu': iletisim_notu,
    })
