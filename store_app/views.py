from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
import datetime


from .models import *
from .utils import cookie_cart, cart_data, anonymous_order


#print('check with true password', customer.user.check_password(password))
#logout(request)

def return_log_in(request):
    return render(request, 'store_app/log_in.html', {})


def return_sign_up(request):
    return render(request, 'store_app/sign_up.html', {})


def log_out(request):
    logout(request)
    return return_store(request)


@csrf_exempt
def process_account(request):
    data = json.loads(request.body.decode('utf-8'))
    action = data['action']

    if action == 'sign_up':
        password = data['password']
        username = data['username']
        email = data['email']
        gender = data['gender']

        customer, account_status = Customer.objects.get_or_create(_username=username)

        if account_status == True:
            new_user = Customer.create_new_user(username=username, email=email, password=password)
            new_user = authenticate(username=username, email=email, password=password)
            customer.user = new_user
            customer.save()
            login(request, new_user)
        else:
            print("Sorry the username or email is taken")

    elif action == 'log_in':
        password = data['password']
        username = data['username']

        customer, account_status = Customer.objects.get_or_create(_username=username)
        if account_status == False:
            customer.user.check_password(password)
            login(request, customer.user)
        else:
            print("Sorry the username or password is incorrect")

    return JsonResponse('User is logged in was done', safe=False)



def return_store(request):
    data = cart_data(request)
    shopping_cart_items = data['shopping_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'shopping_cart_items': shopping_cart_items}
    return render(request, 'store_app/store.html', context)


def return_shopping_cart(request):
    data = cart_data(request)

    shopping_cart_items = data['shopping_cart_items']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}
    return render(request, 'store_app/shopping_cart.html', context)


def return_checkout(request):
    data = cart_data(request)

    shopping_cart_items = data['shopping_cart_items']
    items = data['items']
    order = data['order']

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

    else:
        print("User is not logged in")
        print("Cookies:", request.COOKIES)

        customer, order = anonymous_order(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_price):
        order.complete = True
        order.save()

    if order.shipping == True and request.user.is_authenticated:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode']
        )

    else:
        ShippingAddress.objects.create(
            guest = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode']
        )
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