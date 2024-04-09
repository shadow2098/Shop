from django.shortcuts import render
from .models import *


def return_store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store_app/store.html', context)


def return_shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_price': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store_app/shopping_cart.html', context)


def return_checkout(request):
    return render(request, 'store_app/checkout.html', {})