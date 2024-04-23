from django.db import models
from django.contrib.auth.models import User


class AbstracClass(models.Model):
    class Meta:
        abstract = True

    def return_name(self):
        raise NotImplementedError("Subclasses must implement return_name method")


class Guest(AbstracClass):
    _username = models.CharField(max_length=200, null=False)
    _email = models.CharField(max_length=200, null=False)

    def return_name(self):
        return self._username

class Customer(AbstracClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    _username = models.CharField(max_length=200, null=False)
    _email = models.CharField(max_length=200, null=False)
    _password = models.CharField(max_length=200, null=False)
    _gender = models.CharField(max_length=20, null=True, blank=True)

    def return_name(self):
        return self._username

    @staticmethod
    def create_new_user(username, email, password):
        new_user = User.objects.create_user(username=username, email=email, password=password)
        return new_user


class Product(AbstracClass):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def return_name(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model) :
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def _str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital is False:
                shipping = True
        return shipping

    @property
    def get_cart_price(self):
        orderitems = self.orderitem_set.all()

        total = 0
        for item in orderitems:
            total += item.get_total
        
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()

        total = 0
        for item in orderitems:
            total += item.quantity
        
        return total


class OrderItem(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models. ForeignKey (Order, on_delete=models.SET_NULL, null=True)
    quantity = models. IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress (models.Model):
    customer = models. ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True)
    order = models. ForeignKey (Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models. CharField(max_length=200, null=False)
    zipcode = models. CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address









'''
from django.db import models
from django.contrib.auth.models import User #, UserManager

from overrides import override, EnforceOverrides
from abc import ABC, abstractmethod
'''

'''
class models.User
User objects have the following fields:

username¶
Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.

The max_length should be sufficient for many use cases. If you need a longer length, please use a custom user model. If you use MySQL with the utf8mb4 encoding (recommended for proper Unicode support), specify at most max_length=191 because MySQL can only create unique indexes with 191 characters in that case by default.

first_name¶
Optional (blank=True). 150 characters or fewer.

last_name¶
Optional (blank=True). 150 characters or fewer.

email
Optional (blank=True). Email address.

password
'''
#class Guest(models.Model):
    #username = models.CharField(max_length=200, null=False)
    #email = models.CharField(max_length=200, null=False)

    #def __str__(self):
        #return self.username
'''
class AbstracClass(ABC, EnforceOverrides):

    @abstractmethod
    def return_name(self):
        pass


class Customer(models.Model, AbstracClass):
    class Meta:
        abstract = True

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    _username = models.CharField(max_length=200, null=False)
    _email = models.CharField(max_length=200, null=False)
    _password = models.CharField(max_length=200, null=False)
    _gender = models.CharField(max_length=20, null=True, blank=True)

    @override
    def return_name(self):
        return self.username

    @staticmethod
    def create_new_user(username, email, password):
        new_user = User.objects.create_user(username=username, email=email, password=password)
        return new_user




class Product(models.Model, AbstracClass):
    class Meta:
        abstract = True

    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    @override
    def return_name(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url


class Order(models.Model) :
    customer = models. ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def _str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital is False:
                shipping = True
        return shipping

    @property
    def get_cart_price(self):
        orderitems = self.orderitem_set.all()

        total = 0
        for item in orderitems:
            total += item.get_total
        
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()

        total = 0
        for item in orderitems:
            total += item.quantity
        
        return total


class OrderItem(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models. ForeignKey (Order, on_delete=models.SET_NULL, null=True)
    quantity = models. IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class ShippingAddress (models.Model):
    customer = models. ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models. ForeignKey (Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models. CharField(max_length=200, null=False)
    zipcode = models. CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
'''