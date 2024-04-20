from .models import *
import json

def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print(cart)
    items = []
    order = {'get_cart_price': 0, 'get_cart_items': 0, 'shipping': False}
    shopping_cart_items = order['get_cart_items']

    for i in cart:
        try:
            shopping_cart_items += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = product.price * cart[i]['quantity']

            order['get_cart_price'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image_url,
                },
                'quantity': cart[i]['quantity'],
                'get_cart_price': total
            }
            items.append(item)

            if product.digital == False:
               order['shipping'] = True

        except:
            pass
    return {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shopping_cart_items = order.get_cart_items
    else:
        cookie_data = cookie_cart(request)
        shopping_cart_items = cookie_data['shopping_cart_items']
        items = cookie_data['items']
        order = cookie_data['order']

    return {'items': items, 'order': order, 'shopping_cart_items': shopping_cart_items}


def anonymous_order(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookie_data = cookie_cart(request)
    items = cookie_data['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
        )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
            )
    return customer, order
