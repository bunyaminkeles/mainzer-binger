from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profil/', views.profil, name='profil'),
    path('kullanicilar/', views.kullanici_listesi, name='kullanici_listesi'),
    path('kullanicilar/<str:kullanici_adi>/', views.kullanici_profil, name='kullanici_profil'),
]
