from django.urls import path
from . import views

app_name = 'rehber'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('<slug:slug>/', views.detay, name='detay'),
]
