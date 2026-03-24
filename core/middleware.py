from .models import SiteZiyaret

SESSION_KEY = '_site_ziyaret_sayildi'


class ZiyaretSayaciMiddleware:
    """Her benzersiz oturumu bir kez sayar."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get(SESSION_KEY):
            try:
                SiteZiyaret.artir()
                request.session[SESSION_KEY] = True
            except Exception:
                pass
        return self.get_response(request)
