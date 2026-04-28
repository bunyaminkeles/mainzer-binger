from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

from .models import LocalBusiness, BusinessAnalytics, GlobalSetting

@login_required
def business_dashboard(request):
    # Modülün aktif olup olmadığını kontrol et
    settings = GlobalSetting.load()
    if not settings.is_business_module_active:
        raise Http404

    # Giriş yapmış kullanıcının sahip olduğu işletmeyi bul
    try:
        business = LocalBusiness.objects.get(owner=request.user, is_published=True)
    except LocalBusiness.DoesNotExist:
        business = None
    except LocalBusiness.MultipleObjectsReturned:
        # Bir kullanıcının birden fazla işletmesi varsa ilkini al
        business = LocalBusiness.objects.filter(owner=request.user, is_published=True).first()

    analytics_data = {
        'total_views': 0,
        'total_whatsapp_clicks': 0,
    }

    if business:
        # Son 30 günlük veriyi topla
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        
        data = BusinessAnalytics.objects.filter(
            business=business,
            date__gte=thirty_days_ago
        ).aggregate(
            total_views=Sum('views'),
            total_whatsapp_clicks=Sum('whatsapp_clicks')
        )
        
        # Aggregate sonucu None dönebilir, kontrol et
        analytics_data['total_views'] = data.get('total_views') or 0
        analytics_data['total_whatsapp_clicks'] = data.get('total_whatsapp_clicks') or 0

    context = {
        'business': business,
        'analytics': analytics_data,
        'title': 'İşletme Paneli'
    }
    return render(request, 'businesses/dashboard.html', context)