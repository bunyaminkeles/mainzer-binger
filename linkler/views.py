from django.shortcuts import render, get_object_or_404
from .models import OnemliLink, LINK_KATEGORI

def git(request, pk):
    link = get_object_or_404(OnemliLink, pk=pk, aktif=True)
    return render(request, 'linkler/git.html', {'link': link})

def liste(request):
    kategori = request.GET.get('kategori', '')
    kategoriler = {}
    for k, v in LINK_KATEGORI:
        if k == 'ilan':
            continue  # İlan platformları artık İlanlar sayfasında gösteriliyor
        linkler = OnemliLink.objects.filter(aktif=True, kategori=k)
        if linkler.exists():
            kategoriler[k] = {'ad': v, 'linkler': linkler}
    return render(request, 'linkler/liste.html', {
        'kategoriler': kategoriler,
        'tum_kategoriler': LINK_KATEGORI,
    })
