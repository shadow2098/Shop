from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


from .models import *


def return_store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shopping_cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_price': 0, 'get_cart_items': 0, 'shipping': False}
        shopping_cart_items = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'shopping_cart_items': shopping_cart_items}
    return render(request, 'store_app/store.html', context)


def return_shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shopping_cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_price': 0, 'get_cart_items': 0, 'shipping': False}
        shopping_cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}
    return render(request, 'store_app/shopping_cart.html', context)


def return_checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shopping_cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_price': 0, 'get_cart_items': 0, 'shipping': False}
        shopping_cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}
    return render(request, 'store_app/checkout.html', context)

@csrf_exempt
def update_item(request):
    print(request)
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    product_id = data['product_id']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)

    customer = request.user.customer
    print(customer)
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)

@csrf_exempt
def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body.decode('utf-8'))

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_price):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )
    else:
        print("User is not logged in")
    return JsonResponse('Payment was done', safe=False)
'''
@csrf_protect
def update_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            product_id = data.get('product_id')
            action = data.get('action')
            print('Action:', action)
            print('Product:', product_id)
            
            # Return a JSON response with a success message
            return JsonResponse({'message': 'Item was updated successfully'}, status=200)
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Handle invalid request method
        return JsonResponse({'error': 'Invalid request method'}, status=405)
'''