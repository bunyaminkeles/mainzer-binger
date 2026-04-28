from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    # Örnek:
    # path('', views.business_list_view, name='list'),
    
    path('dashboard/', views.business_dashboard, name='dashboard'),
]