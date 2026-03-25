from django.shortcuts import render, get_object_or_404, redirect
from .models import Kaynak, KAYNAK_KATEGORI


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        qs = Kaynak.objects.filter(stadt=stadt, scope='stadt', yayinda=True)
    else:
        qs = Kaynak.objects.filter(scope='eyalet', eyalet__slug=eyalet_slug, yayinda=True)

    kategoriler = {}
    for k, v in KAYNAK_KATEGORI:
        kaynaklar = qs.filter(kategori=k)
        if kaynaklar.exists():
            kategoriler[v] = kaynaklar

    return render(request, 'rehber/liste.html', {
        'kategoriler':  kategoriler,
        'stadt':        stadt,
        'eyalet_slug':  eyalet_slug,
    })


def anabin_widget(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'rehber/anabin_widget.html', {
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


def detay(request, slug, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    if not slug or slug == 'None':
        if stadt_slug:
            return redirect(f'/{eyalet_slug}/{stadt_slug}/rehber/')
        return redirect(f'/{eyalet_slug}/rehber/')

    kaynak = get_object_or_404(Kaynak, slug=slug, yayinda=True)
    if kaynak.tip == 'link':
        return redirect(kaynak.url)

    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'rehber/detay.html', {
        'sayfa':       kaynak,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
