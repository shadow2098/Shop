from django.urls import path
from . import views


urlpatterns = [
    path('', views.return_store, name='store'),
    path('shopping_cart/', views.return_shopping_cart, name='shopping_cart'),
    path('checkout/', views.return_checkout, name='checkout'),
    path('log_in/', views.return_log_in, name='log_in'),
    path('update_item/', views.update_item, name='update_item'),
    path('process_order/', views.process_order, name='process_order'),
]