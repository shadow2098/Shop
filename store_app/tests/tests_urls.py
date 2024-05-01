import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import return_store, return_shopping_cart, update_item, return_checkout, process_order, add_product, add_product_process, return_log_in, return_sign_up, log_out, process_account, return_seller_log_in, return_seller_sign_up, export_all_usernames


class TestUrls(SimpleTestCase):
    
    def test_store_url_resolves(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func, return_store)

    def test_shopping_cart_url_resolves(self):
        url = reverse('shopping_cart')
        self.assertEquals(resolve(url).func, return_shopping_cart)


    def test_update_item_url_resolves(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func, update_item)


    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, return_checkout)


    def test_process_order_url_resolves(self):
        url = reverse('process_order')
        self.assertEquals(resolve(url).func, process_order)


    def test_add_product_url_resolves(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)


    def test_add_product_process_url_resolves(self):
        url = reverse('add_product_process')
        self.assertEquals(resolve(url).func, add_product_process)


    def test_log_in_url_resolves(self):
        url = reverse('log_in')
        self.assertEquals(resolve(url).func, return_log_in)


    def test_sign_up_url_resolves(self):
        url = reverse('sign_up')
        self.assertEquals(resolve(url).func, return_sign_up)


    def test_log_out_url_resolves(self):
        url = reverse('log_out')
        self.assertEquals(resolve(url).func, log_out)


    def test_process_account_url_resolves(self):
        url = reverse('process_account')
        self.assertEquals(resolve(url).func, process_account)


    def test_seller_log_in_url_resolves(self):
        url = reverse('seller_log_in')
        self.assertEquals(resolve(url).func, return_seller_log_in)


    def test_seller_sign_up_url_resolves(self):
        url = reverse('seller_sign_up')
        self.assertEquals(resolve(url).func, return_seller_sign_up)


    def test_export_url_resolves(self):
        url = reverse('export')
        self.assertEquals(resolve(url).func, export_all_usernames)