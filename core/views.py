from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from duyurular.models import Duyuru
from blog.models import BlogYazisi
from ilan.models import Ilan
from takvim.models import Etkinlik
from django.utils import timezone


def anasayfa(request):
    son_duyurular = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:4]
    son_yazilar   = BlogYazisi.objects.filter(yayinda=True).order_by('-olusturulma')[:3]
    son_ilanlar   = Ilan.objects.filter(aktif=True).order_by('-olusturulma')[:4]
    yaklasan      = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:3]
    return render(request, 'core/anasayfa.html', {
        'son_duyurular': son_duyurular,
        'son_yazilar':   son_yazilar,
        'son_ilanlar':   son_ilanlar,
        'yaklasan':      yaklasan,
    })


def hakkinda(request):
    return render(request, 'core/hakkinda.html')


def iletisim(request):
    return render(request, 'core/iletisim.html')


@login_required
def dashboard(request):
    son_duyurular = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan      = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:5]
    benim_ilanim  = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    return render(request, 'core/dashboard.html', {
        'son_duyurular': son_duyurular,
        'yaklasan':      yaklasan,
        'benim_ilanim':  benim_ilanim,
    })
