from django.urls import path
from . import views


urlpatterns = [
    path('', views.return_store, name='store'),
    path('shopping_cart/', views.return_shopping_cart, name='shopping_cart'),
    path('checkout/', views.return_checkout, name='checkout'),
    path('update_item/', views.update_item, name='update_item'),
]