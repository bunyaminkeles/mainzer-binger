from django.urls import path
from . import views

app_name = 'ilan'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('ver/', views.ilan_ver, name='ver'),
    path('<int:pk>/', views.detay, name='detay'),
]
