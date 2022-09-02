from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('semana1/', views.about, name="semana1"),
    path('semana2/', views.services, name="semana2"),
    path('semana3/', views.contact, name="semana3"),
    path('dependencias/', views.blog, name="dependencias"),
    path('metas/', views.sample, name="metas"),
]