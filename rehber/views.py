from django.shortcuts import render, get_object_or_404
from .models import Kaynak, KAYNAK_KATEGORI

def liste(request):
    kategoriler = {}
    for k, v in KAYNAK_KATEGORI:
        kaynaklar = Kaynak.objects.filter(kategori=k, yayinda=True)
        if kaynaklar.exists():
            kategoriler[v] = kaynaklar
    return render(request, 'rehber/liste.html', {'kategoriler': kategoriler})

def detay(request, slug):
    kaynak = get_object_or_404(Kaynak, slug=slug, yayinda=True)
    return render(request, 'rehber/detay.html', {'sayfa': kaynak})
