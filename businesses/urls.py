from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.business_list, name='list'),
    path('<slug:slug>/track/', views.track_business_click, name='track'),
]
