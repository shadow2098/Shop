from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseForbidden
from itertools import chain
from django.core.files.uploadedfile import SimpleUploadedFile


import datetime
import json

from .utils import cookie_cart, cart_data, anonymous_order
from .models import *

@login_required
def add_product(request):
    try:
        if request.user.seller.is_a_seller:
            return render(request, 'store_app/add_product.html')

    except:
        return render(request, 'store_app/cannot_enter_customer.html')

@csrf_exempt
def add_product_process(request):
    data = json.loads(request.body.decode('utf-8'))
    name = data['name']
    price = data['price']
    digital = False
    image = data['image']
    print(image)

    print("HJHVHS   JHDH    BHBJ    BDHJDBJQJHJBQJDBQ")
    if digital is None:
        digital = False

    product = Product.objects.create(
        name=name,
        price=price,
        digital=digital,
        image=image
    )
    product.save()

    if hasattr(request.user, 'seller'):
        seller = request.user.seller
        if seller.my_products:
            seller.my_products += str(product.id) + ' '
        else:
            seller.my_products = str(product.id) + ' '
        seller.save()

        return JsonResponse({'success': True})

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def export_all_usernames(request):
    customer_list = Customer.objects.all()
    guest_list = Guest.objects.all()
    print(guest_list)

    result_list = chain(customer_list, guest_list)

    i = 0
    customer_len = len(list(customer_list))

    f = open('store_app/templates/store_app/usernames.txt', 'w')
    f.write('Customers:\n')
    for obj in result_list:
        i += 1
        if i == customer_len:
            f.write('Guests:\n')
        f.write('   ' + str(obj._username) + '\n')
        f.write('\n')

    f.close()
    return redirect('/usernames.txt/')


def return_log_in(request):
    return render(request, 'store_app/log_in.html', {})


def return_seller_log_in(request):
    return render(request, 'store_app/seller_log_in.html', {})


def return_seller_sign_up(request):
    return render(request, 'store_app/seller_sign_up.html', {})


def return_sign_up(request):
    return render(request, 'store_app/sign_up.html', {})

@login_required
def log_out(request):
    logout(request)
    return return_store(request)


@csrf_exempt
def process_account(request):
    data = json.loads(request.body.decode('utf-8'))
    action = data['action']
    seller_status = data['seller']


    if action == 'sign_up':
        password = data['password']
        username = data['username']
        email = data['email']

        if seller_status == 'yes':
            seller, account_status = Seller.objects.get_or_create(_username=username)

            if account_status == True:
                new_user = Seller.create_new_user(username=username, email=email, password=password)
                new_user = authenticate(username=username, email=email, password=password, last_name='seller')
                seller.user = new_user
                seller.save()
                login(request, new_user)
            else:
                print("Sorry the username or email is taken")

        elif seller_status == 'no':
            gender = data['gender']

            customer, account_status = Customer.objects.get_or_create(_username=username)

            if account_status == True:
                new_user = Customer.create_new_user(username=username, email=email, password=password)
                new_user = authenticate(username=username, email=email, password=password, last_name='not_seller')
                customer.user = new_user
                customer.save()
                customer._gender = gender
                customer.save()
                login(request, new_user)
            else:
                print("Sorry the username or email is taken")


    elif action == 'log_in':
        password = data['password']
        username = data['username']

        if seller_status == 'yes':
            seller, account_status = Seller.objects.get_or_create(_username=username)
            if account_status == False:
                if seller.user.check_password(password):
                    seller.user = authenticate(username=username, password=password, last_name='seller')
                    login(request, seller.user)
                else:
                    print("Sorry wrong password or username")
            else:
                print("Sorry the username or password is incorrect")

        elif seller_status == 'no':
            customer, account_status = Customer.objects.get_or_create(_username=username)
            if account_status == False:
                if customer.user.check_password(password):
                    customer.user = authenticate(username=username, password=password, last_name='not_seller')
                    login(request, customer.user)
                else:
                    print("Sorry wrong password or username")
            else:
                print("Sorry the username or password is incorrect")

    return JsonResponse('User is logged in was done', safe=False)



def return_store(request):
    try:
        if request.user.seller.is_a_seller:
            my_str = request.user.seller.my_products
            if my_str is None:
                context = {}
            else:
                product_id_list = my_str.split(' ')
                product_id_list.pop(-1)
                my_product_list = []
                for i in range(len(product_id_list)):
                    my_product_list.append((Product.objects.get(id=product_id_list[i])))

                context = {'products': my_product_list}
            return render(request, 'store_app/store.html', context)

    except:
        data = cart_data(request)
        shopping_cart_items = data['shopping_cart_items']
        products = Product.objects.all()

        context = {'products': products, 'shopping_cart_items': shopping_cart_items}
        return render(request, 'store_app/store.html', context)


def return_shopping_cart(request):
    try:
        if request.user.seller.is_a_seller:
            return render(request, 'store_app/cannot_enter_seller.html')
    except:
        data = cart_data(request)

        shopping_cart_items = data['shopping_cart_items']
        items = data['items']
        order = data['order']

        context = {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}
        return render(request, 'store_app/shopping_cart.html', context)


def return_checkout(request):
    try:
        if request.user.seller.is_a_seller:
            return render(request, 'store_app/cannot_enter_seller.html')
    except:
        data = cart_data(request)

        shopping_cart_items = data['shopping_cart_items']
        items = data['items']
        order = data['order']

        context = {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}
        return render(request, 'store_app/checkout.html', context)


@csrf_exempt
def update_item(request):
    data = json.loads(request.body.decode('utf-8'))

    product_id = data['product_id']
    action = data['action']

    customer = request.user.customer
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