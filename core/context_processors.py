from .models import SiteZiyaret


def ziyaret_sayisi(request):
    try:
        return {'ziyaret_sayisi': SiteZiyaret.sayac()}
    except Exception:
        return {'ziyaret_sayisi': 0}
