import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import F
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import LocalBusiness, BusinessAnalytics


def business_list(request):
    today = timezone.localdate()
    aktif_isletmeler = (
        LocalBusiness.objects
        .filter(is_published=True, end_date__gte=today)
        .select_related('city', 'category', 'subscription_plan')
        .order_by('category__name', 'name')
    )

    # Kategorilere göre grupla
    kategoriler = []
    seen = {}
    for isletme in aktif_isletmeler:
        cat = isletme.category
        cat_id = cat.id if cat else 0
        if cat_id not in seen:
            seen[cat_id] = {'kategori': cat, 'isletmeler': []}
            kategoriler.append(seen[cat_id])
        seen[cat_id]['isletmeler'].append(isletme)

    return render(request, 'businesses/business_list.html', {
        'kategoriler': kategoriler,
        'toplam': aktif_isletmeler.count(),
    })


@require_POST
def track_business_click(request, slug):
    business = get_object_or_404(LocalBusiness, slug=slug, is_published=True)

    try:
        payload = json.loads(request.body)
        action = payload.get('action', '')
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'status': 'error', 'message': 'Geçersiz JSON'}, status=400)

    if action not in ('view', 'whatsapp'):
        return JsonResponse({'status': 'error', 'message': 'Geçersiz action'}, status=400)

    record, _ = BusinessAnalytics.objects.get_or_create(
        business=business,
        date=timezone.localdate(),
    )

    if action == 'view':
        BusinessAnalytics.objects.filter(pk=record.pk).update(views=F('views') + 1)
    else:
        BusinessAnalytics.objects.filter(pk=record.pk).update(whatsapp_clicks=F('whatsapp_clicks') + 1)

    return JsonResponse({'status': 'ok'})
