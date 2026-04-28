from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('bulten-kayit/', views.bulten_kayit_api, name='bulten_kayit'),
    path('sehir-ara/', views.sehir_ara, name='sehir_ara'),
    path('health/', views.health, name='health'),
    path('run/rss-cek/', views.rss_cek, name='run_rss_cek'),
    path('run/cleanup-s3/', views.cleanup_s3, name="run_cleanup_s3"),
    path('run/seed/', views.seed_calistir, name="run_seed"),

    # Yeni eklenen endpoint
    path('businesses/analytics/', views.business_analytics_api, name='business_analytics_api'),
]