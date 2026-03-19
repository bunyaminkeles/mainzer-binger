import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings
from django.core.management import call_command


def health(request):
    """Basit health check — cron-job.org veya uptime monitörler için."""
    return JsonResponse({
        'status': 'ok',
        'timestamp': timezone.now().isoformat(),
        'service': 'mainzer-binger',
    })


@csrf_exempt
def rss_cek(request):
    """
    RSS ve scraping görevini tetikler.
    GET veya POST ile çağrılabilir.
    ?token=<CRON_SECRET> veya Authorization: Bearer <CRON_SECRET> header'ı gerekli.
    """
    # Token doğrulama
    secret = getattr(settings, 'CRON_SECRET', None)
    if not secret:
        return JsonResponse({'error': 'CRON_SECRET ayarlanmamış.'}, status=500)

    token = (
        request.GET.get('token')
        or request.POST.get('token')
        or request.headers.get('Authorization', '').removeprefix('Bearer ').strip()
    )
    if token != secret:
        return JsonResponse({'error': 'Yetkisiz.'}, status=401)

    try:
        # stdout/stderr'ı yakala
        from io import StringIO
        out = StringIO()
        call_command('rss_cek', stdout=out, stderr=out)
        return JsonResponse({
            'status': 'ok',
            'timestamp': timezone.now().isoformat(),
            'output': out.getvalue(),
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'detail': str(e)}, status=500)
