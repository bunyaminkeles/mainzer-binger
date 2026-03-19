from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ForumKategori, Konu, Yorum

def liste(request):
    kategoriler = ForumKategori.objects.prefetch_related('konular').all()
    return render(request, 'forum/liste.html', {'kategoriler': kategoriler})

def konu_detay(request, pk):
    konu = get_object_or_404(Konu, pk=pk)
    yorumlar = konu.yorumlar.select_related('yazar').all()
    return render(request, 'forum/konu.html', {'konu': konu, 'yorumlar': yorumlar})

@login_required
def yorum_ekle(request, pk):
    konu = get_object_or_404(Konu, pk=pk)
    if not konu.kapali and request.method == 'POST':
        Yorum.objects.create(konu=konu, yazar=request.user, icerik=request.POST['icerik'])
    return redirect('forum:konu', pk=pk)

@login_required
def konu_ac(request, kategori_pk):
    kategori = get_object_or_404(ForumKategori, pk=kategori_pk)
    if request.method == 'POST':
        konu = Konu.objects.create(
            kategori=kategori,
            yazar=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
        )
        messages.success(request, 'Konu açıldı.')
        return redirect('forum:konu', pk=konu.pk)
    return render(request, 'forum/konu_ac.html', {'kategori': kategori})
