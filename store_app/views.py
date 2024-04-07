from django.shortcuts import render
from .models import *


def return_store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store_app/store.html', context)


def return_shopping_cart(request):
    return render(request, 'store_app/shopping_cart.html', {})


def return_checkout(request):
    return render(request, 'store_app/checkout.html', {})