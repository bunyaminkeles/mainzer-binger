from django.shortcuts import render, get_object_or_404
from .models import RehberSayfasi, REHBER_KATEGORI

def liste(request):
    kategoriler = {}
    for k, v in REHBER_KATEGORI:
        sayfalar = RehberSayfasi.objects.filter(kategori=k, yayinda=True)
        if sayfalar.exists():
            kategoriler[v] = sayfalar
    return render(request, 'rehber/liste.html', {'kategoriler': kategoriler})

def detay(request, slug):
    sayfa = get_object_or_404(RehberSayfasi, slug=slug, yayinda=True)
    return render(request, 'rehber/detay.html', {'sayfa': sayfa})
