from django.shortcuts import render
from .models import Etkinlik
from django.utils import timezone

def liste(request):
    etkinlikler = Etkinlik.objects.filter(tarih__gte=timezone.now().date())
    return render(request, 'takvim/liste.html', {'etkinlikler': etkinlikler})

# alias
takvim = liste
