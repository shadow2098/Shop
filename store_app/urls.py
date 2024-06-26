from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.return_store, name='store'),
    path('shopping_cart/', views.return_shopping_cart, name='shopping_cart'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/', views.return_checkout, name='checkout'),
    path('process_order/', views.process_order, name='process_order'),

    path('add_product/', views.add_product, name='add_product'),
    path('add_product_process/', views.add_product_process, name='add_product_process'),

    path('log_in/', views.return_log_in, name='log_in'),
    path('sign_up/', views.return_sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('process_account/', views.process_account, name='process_account'),

    path('seller_log_in/', views.return_seller_log_in, name='seller_log_in'),
    path('seller_sign_up/', views.return_seller_sign_up, name='seller_sign_up'),

    path('export/', views.export_all_usernames, name='export'),
    path('usernames.txt/', TemplateView.as_view(template_name='store_app/usernames.txt', content_type='text/plain')),
]