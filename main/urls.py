from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.item),
    path('order/<slug:user>/', views.order),
    path('orders/', views.orders, name='orders'),
    path('allorders/', views.allorders, name='allorders'),
]
