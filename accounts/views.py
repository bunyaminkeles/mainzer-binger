from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profil
from ilan.models import Ilan
from django.utils import timezone
from takvim.models import Etkinlik
from duyurular.models import Duyuru
from forum.models import Konu
from blog.models import BlogYazisi

@login_required
def dashboard(request):
    from stadt.models import Stadt
    profil, _ = Profil.objects.get_or_create(kullanici=request.user)

    # Kullanıcının şehrini bul, yoksa ilk aktif şehri kullan
    stadt = Stadt.objects.select_related('eyalet').filter(aktiv=True).first()

    son_duyurular  = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan       = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:5]
    benim_ilanim   = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    son_konular    = Konu.objects.select_related('yazar', 'kategori').order_by('-guncelleme')[:5]
    son_bloglar    = BlogYazisi.objects.filter(yayinda=True).order_by('-olusturulma')[:3]
    benim_konularim = Konu.objects.filter(yazar=request.user).count()
    eyalet_slug = stadt.eyalet.slug if stadt and stadt.eyalet else 'rlp'
    return render(request, 'core/dashboard.html', {
        'profil': profil,
        'stadt': stadt,
        'eyalet_slug': eyalet_slug,
        'son_duyurular': son_duyurular,
        'yaklasan': yaklasan,
        'benim_ilanim': benim_ilanim,
        'son_konular': son_konular,
        'son_bloglar': son_bloglar,
        'benim_konularim': benim_konularim,
    })

@login_required
def profil(request):
    p, _ = Profil.objects.get_or_create(kullanici=request.user)
    if request.method == 'POST':
        p.biyografi       = request.POST.get('biyografi', '')
        p.sehir           = request.POST.get('sehir', '')
        p.biyografi_gizli = 'biyografi_gizli' in request.POST
        p.sehir_gizli     = 'sehir_gizli' in request.POST
        p.save()
        return redirect('accounts:dashboard')
    return render(request, 'accounts/profil.html', {'profil': p})


def kullanici_listesi(request):
    q = request.GET.get('q', '').strip()
    kullanicilar = User.objects.filter(is_active=True).select_related('profil').order_by('username')
    if q:
        kullanicilar = kullanicilar.filter(username__icontains=q)
    return render(request, 'accounts/kullanici_listesi.html', {
        'kullanicilar': kullanicilar,
        'q': q,
    })


def kullanici_profil(request, kullanici_adi):
    hedef = get_object_or_404(User, username=kullanici_adi, is_active=True)
    profil, _ = Profil.objects.get_or_create(kullanici=hedef)
    return render(request, 'accounts/kullanici_profil.html', {
        'hedef': hedef,
        'profil': profil,
    })
