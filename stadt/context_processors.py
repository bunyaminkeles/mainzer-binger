from .models import Stadt, Eyalet


def alle_staedte(request):
    """Tüm aktif şehirleri ve eyaletleri her template'e sağlar (navbar dropdown için)."""
    return {
        'alle_staedte':   Stadt.objects.filter(aktiv=True).select_related('eyalet').order_by('name'),
        'alle_eyaletler': Eyalet.objects.filter(aktif=True).order_by('ad'),
    }
