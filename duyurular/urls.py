from django.urls import path
from . import views

app_name = 'duyurular'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('ekle/', views.duyuru_ekle, name='duyuru_ekle'),
    path('<int:pk>/', views.detay, name='detay'),
]
