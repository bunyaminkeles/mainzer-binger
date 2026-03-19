from django.urls import path
from . import views

app_name = 'linkler'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('git/<int:pk>/', views.git, name='git'),
]
