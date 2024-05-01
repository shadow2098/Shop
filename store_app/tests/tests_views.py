import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
import json
import uuid

from ..models import Guest, Customer, Seller, Product, Order, OrderItem, ShippingAddress


class ViewsTest(TestCase):
    def setUp(self):
        self.username = str(uuid.uuid4())[:8]

        self.user = User.objects.create_user(username=self.username, password='password')

        self.seller = Seller.objects.create(user=self.user, _username=self.username, _email='testemail')

        self.product_data = {
            'name': 'Test Product',
            'price': 10.0,
            'image': 'test_image.jpg'
        }
        self.product = Product.objects.create(
            name=self.product_data['name'],
            price=self.product_data['price'],
            digital=False,
            image=self.product_data['image']
        )

        self.guest = Guest.objects.create(_username=self.username, _email='testmail')

        self.customer = Customer.objects.create(user=self.user, _username=self.username, _email='testmail', _password='password', _gender='no')

        self.client = Client()

    def test_add_product_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/add_product.html')

        self.client.logout()
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'store_app/cannot_enter_customer.html')


    def test_add_product_process_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('add_product_process'), json.dumps(self.product_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

        self.client.logout()
        response = self.client.post(reverse('add_product_process'), json.dumps(self.product_data), content_type='application/json')
        self.assertEqual(response.status_code, 405)

    def test_export_all_usernames_view(self):
        response = self.client.get(reverse('export'))
        self.assertEqual(response.status_code, 302)

    def test_return_log_in_view(self):
        response = self.client.get(reverse('log_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/log_in.html')

    def test_return_seller_log_in_view(self):
        response = self.client.get(reverse('seller_log_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/seller_log_in.html')

    def test_return_seller_sign_up_view(self):
        response = self.client.get(reverse('seller_sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/seller_sign_up.html')

    def test_return_sign_up_view(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/sign_up.html')

    def test_log_out_view(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('log_out'))
        self.assertEqual(response.status_code, 302)


    def test_process_account_view(self):
        data = {
            'action': 'sign_up',
            'username': self.username,
            'password': 'password',
            'email': 'test@example.com',
            'seller': 'yes'
        }
        response = self.client.post(reverse('process_account'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Seller.objects.filter(user__username=self.username).exists())


        data['action'] = 'log_in'
        response = self.client.post(reverse('process_account'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User is logged in was done')

    def test_return_store_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/store.html')

        self.client.logout()
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/store.html')

    def test_urls(self):
        self.assertEqual(reverse('add_product'), '/add_product/')
        self.assertEqual(reverse('add_product_process'), '/add_product_process/')
        self.assertEqual(reverse('export'), '/export/')
        self.assertEqual(reverse('log_in'), '/log_in/')
        self.assertEqual(reverse('sign_up'), '/sign_up/')
        self.assertEqual(reverse('log_out'), '/log_out/')
        self.assertEqual(reverse('process_account'), '/process_account/')