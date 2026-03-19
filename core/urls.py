from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('hakkinda/', views.hakkinda, name='hakkinda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
