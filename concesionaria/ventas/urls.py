from django.urls import path

from ventas import views

urlpatterns = [
    path('',views.ventas,name='ventas'),
]