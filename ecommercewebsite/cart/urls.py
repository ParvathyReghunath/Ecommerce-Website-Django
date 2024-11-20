from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart_summary/', views.cart_summary, name='cart_summary'),  # Added trailing slash
    path('add/', views.cart_add, name='cart_add'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_delete, name='cart_delete'),
]
