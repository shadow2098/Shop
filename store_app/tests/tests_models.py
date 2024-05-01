import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from django.contrib.auth.models import User
from django.test import TestCase
import uuid

from ..models import Guest, Customer, Seller, Product, Order, OrderItem, ShippingAddress


class TestModels(TestCase):
    def setUp(self):
        self.username = str(uuid.uuid4())[:8]

    def test_guest_model(self):
        guest = Guest.objects.create(_username=self.username, _email="test@example.com")
        self.assertEqual(guest.return_name(), self.username)

    def test_customer_model(self):
        user = User.objects.create_user(username=self.username, email="test@example.com", password="password")
        customer = Customer.objects.create(user=user, _username=self.username, _email="test@example.com", _password="password", _gender="no")
        self.assertEqual(customer.return_name(), self.username)

    def test_seller_model(self):
        user = User.objects.create_user(username=self.username, email="test@example.com", password="password")
        seller = Seller.objects.create(user=user, _username=self.username, _email="test@example.com", _password="password")
        self.assertEqual(seller.return_name(), self.username)

    def test_product_model(self):
        product = Product.objects.create(name="Test Product", price=10.0)
        self.assertEqual(product.return_name(), "Test Product")

    def test_order_model(self):
        order = Order.objects.create()
        self.assertIsNone(order.customer)
        self.assertIsNone(order.guest)
        self.assertFalse(order.complete)

    def test_order_item_model(self):
        product = Product.objects.create(name="Test Product", price=10.0)
        order = Order.objects.create()
        order_item = OrderItem.objects.create(product=product, order=order, quantity=2)
        self.assertEqual(order_item.get_total, 20.0)

    def test_shipping_address_model(self):
        order = Order.objects.create()
        shipping_address = ShippingAddress.objects.create(
            order=order, address="123 Test St", city="Test City", state="Test State", zipcode="12345"
        )
        self.assertEqual(str(shipping_address), "123 Test St")