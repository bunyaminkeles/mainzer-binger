from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ilan, ILAN_KATEGORI

def liste(request):
    kategori = request.GET.get('kategori', '')
    qs = Ilan.objects.filter(aktif=True, onaylandi=True)
    if kategori:
        qs = qs.filter(kategori=kategori)
    return render(request, 'ilan/liste.html', {'ilanlar': qs, 'kategoriler': ILAN_KATEGORI, 'secili': kategori})

def detay(request, pk):
    ilan = get_object_or_404(Ilan, pk=pk, aktif=True, onaylandi=True)
    return render(request, 'ilan/detay.html', {'ilan': ilan})

@login_required
def ilan_ver(request):
    if request.method == 'POST':
        ilan = Ilan(
            sahip=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
            kategori=request.POST['kategori'],
            iletisim=request.POST['iletisim'],
        )
        fiyat = request.POST.get('fiyat')
        if fiyat:
            ilan.fiyat = fiyat
        ilan.save()
        messages.success(request, 'İlanınız alındı, inceleme sonrası yayınlanacaktır.')
        return redirect('ilan:liste')
    return render(request, 'ilan/ilan_ver.html', {'kategoriler': ILAN_KATEGORI})
