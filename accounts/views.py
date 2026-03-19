from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profil
from ilan.models import Ilan
from django.utils import timezone
from takvim.models import Etkinlik
from duyurular.models import Duyuru

@login_required
def dashboard(request):
    profil, _ = Profil.objects.get_or_create(kullanici=request.user)
    son_duyurular = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan      = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:5]
    benim_ilanim  = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    return render(request, 'core/dashboard.html', {
        'profil': profil,
        'son_duyurular': son_duyurular,
        'yaklasan': yaklasan,
        'benim_ilanim': benim_ilanim,
    })

@login_required
def profil(request):
    p, _ = Profil.objects.get_or_create(kullanici=request.user)
    if request.method == 'POST':
        p.biyografi = request.POST.get('biyografi', '')
        p.sehir     = request.POST.get('sehir', 'Mainz')
        p.save()
        return redirect('accounts:dashboard')
    return render(request, 'accounts/profil.html', {'profil': p})
