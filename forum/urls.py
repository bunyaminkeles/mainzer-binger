from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('konu/<int:pk>/', views.konu_detay, name='konu'),
    path('konu/<int:pk>/yorum/', views.yorum_ekle, name='yorum_ekle'),
    path('kategori/<int:kategori_pk>/yeni/', views.konu_ac, name='konu_ac'),
]
