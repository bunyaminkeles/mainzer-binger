from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Stadt, Eyalet
from duyurular.models import Duyuru
from blog.models import BlogYazisi
from ilan.models import Ilan
from takvim.models import Etkinlik
from forum.models import Konu
from django.utils import timezone


def eyalet_home(request, eyalet_slug='rlp'):
    eyalet = get_object_or_404(Eyalet, slug=eyalet_slug, aktif=True)
    sehirler = Stadt.objects.filter(eyalet=eyalet, aktiv=True).order_by('name')

    son_duyurular = Duyuru.objects.filter(
        scope='eyalet', eyalet=eyalet, yayinda=True
    ).order_by('-olusturulma')[:5]

    son_konular = Konu.objects.filter(
        scope='eyalet', eyalet=eyalet
    ).select_related('yazar').order_by('-olusturulma')[:6]

    son_yazilar = BlogYazisi.objects.filter(
        scope='eyalet', eyalet=eyalet, yayinda=True
    ).order_by('-olusturulma')[:4]

    son_ilanlar = Ilan.objects.filter(
        scope='eyalet', eyalet=eyalet, aktif=True, onaylandi=True
    ).order_by('-olusturulma')[:4]

    yaklasan = Etkinlik.objects.filter(
        scope='eyalet', eyalet=eyalet,
        tarih__gte=timezone.now().date()
    ).order_by('tarih')[:4]

    return render(request, 'eyalet/home.html', {
        'eyalet':        eyalet,
        'eyalet_slug':   eyalet_slug,
        'sehirler':      sehirler,
        'son_duyurular': son_duyurular,
        'son_konular':   son_konular,
        'son_yazilar':   son_yazilar,
        'son_ilanlar':   son_ilanlar,
        'yaklasan':      yaklasan,
    })


def home(request, eyalet_slug='rlp', stadt_slug=None):
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)

    son_duyurular = Duyuru.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        yayinda=True
    ).order_by('-olusturulma')[:4]

    son_yazilar = BlogYazisi.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        yayinda=True
    ).order_by('-olusturulma')[:3]

    son_ilanlar = Ilan.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        aktif=True, onaylandi=True
    ).order_by('-olusturulma')[:4]

    yaklasan = Etkinlik.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        tarih__gte=timezone.now().date()
    ).order_by('tarih')[:3]

    return render(request, 'stadt/home.html', {
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
        'son_duyurular': son_duyurular,
        'son_yazilar':   son_yazilar,
        'son_ilanlar':   son_ilanlar,
        'yaklasan':      yaklasan,
    })
