from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.business_list, name='list'),
    path('dashboard/', views.business_dashboard, name='dashboard'), # Bu satırı yukarı taşıdık
    path('<slug:slug>/track/', views.track_business_click, name='track'),
    path('<slug:kategori_slug>/', views.category_list, name='category_list'),
]
