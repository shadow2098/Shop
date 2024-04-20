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