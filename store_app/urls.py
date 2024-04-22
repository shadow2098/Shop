from django.urls import path
from . import views


urlpatterns = [
    path('', views.return_store, name='store'),
    path('shopping_cart/', views.return_shopping_cart, name='shopping_cart'),
    path('checkout/', views.return_checkout, name='checkout'),
    path('log_in/', views.return_log_in, name='log_in'),
    path('sign_up/', views.return_sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('process_sign_up/', views.process_sign_up, name='process_sign_up'),
    path('update_item/', views.update_item, name='update_item'),
    path('process_order/', views.process_order, name='process_order'),
]