## What is this program?
This is an online shop application written using Django framework. The aim was to create an online shop for users to be able to use.
 For person you be able to shop, they can either create an account using Log In button in the up right corner OR they can shop as guest without an account. 
 Both guest and logged in user can add products to their shopping cart and check out with the chosen products  
Also, person can create a seller account, and be able to add a product for the customers to buy. **Seller does not have access to the shopping cart**

## How to run the program?
First off, clone the repository. Then enter the Shop folder ($/Shop).  
Run the command `python manage.py migrate` <-- This will create a database for you.  
Then, run `python manage.py createsuperuser`. ***Make sure to remember the info of your superuser*** (Visit this link if something goes wrong https://www.geeksforgeeks.org/how-to-create-superuser-in-django/)    

To start the local server, run `python manage.py runserver`. And enter http://127.0.0.1:8000/ . The store page is now empty, but that's fine since database is empty too.

### How to add products? 
1) Enter http://127.0.0.1:8000/admin/ , enter your superuser info, and click the same button as in the image below  
Note: You can use pictures from store_app/static/store_app/images/ for test products 
<img width="1440" alt="admin" src="https://github.com/shadow2098/Shop/assets/93429735/21c1159a-85a4-435e-a55b-f0cfa1ab2cd2">
And fill out the form for the product creation.    
  
2) You can also add products by creating seller account. ***Note: Log out as a superuser in the admin panel before entering http://127.0.0.1:8000/***

Click "Log in" in the up right corner of the http://127.0.0.1:8000/ -> Click "Log in as seller" -> Click sign up as seller. After that go to click "Add product button" and fill out the form. You should be able to see you product apprear in the catalog on main page


# Coursework requirements

### Abstraction and Inheritance
store_app/models.py line 5 is abstract class, and then Guest, Customer, Seller, and Product are children of abstarct class  
Example:
```ruby
class AbstracClass(models.Model):
    class Meta:`
        abstract = True

    def return_name(self):`
        raise NotImplementedError("Subclasses must implement return_name method")


class Guest(AbstracClass):
    _username = models.CharField(max_length=200, null=False)
    _email = models.CharField(max_length=200, null=False)
    is_a_seller = False

    def return_name(self):
        return self._username
```
### Encapsulation
store_app/models.py Guest, Customer, and Seller classes have _ (protected) fields, and by default fields are also private inside django models
Example:
```ruby
class Customer(AbstracClass):`
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    _username = models.CharField(max_length=200, null=False)
    _email = models.CharField(max_length=200, null=False)
    _password = models.CharField(max_length=200, null=False)
    _gender = models.CharField(max_length=20, null=True, blank=True)
    is_a_seller = False
```

### Polymorphism and writing to file
store_app/views.py line 63 is a function where we treat Guest, Customer, and Seller objects as same type and write all usernames into the file
Example:
```ruby
def export_all_usernames(request):
    customer_list = Customer.objects.all()
    guest_list = Guest.objects.all()
    seller_list = Seller.objects.all()

    result_list = chain(customer_list, guest_list, seller_list)

    i = 0
    c_len = len(list(customer_list))
    g_c_len = c_len + len(list(seller_list))

    f = open('store_app/templates/store_app/usernames.txt', 'w')
    f.write('Customers:\n')
    for obj in result_list:
        i += 1
        if i == c_len:
            f.write('Guests:\n')
        if i == g_c_len:
            f.write('Sellers:\n')
        f.write('   ' + str(obj._username) + '\n')
        f.write('\n')

    f.close()
    return redirect('/usernames.txt/')
```

### Decorator
Different decorators are used throughout store_app/views.py
Example:
```ruby
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def add_product(request):
    try:
        if request.user.seller.is_a_seller:
            return render(request, 'store_app/add_product.html')

    except:
        return render(request, 'store_app/cannot_enter_customer.html')

@csrf_exempt
def process_account(request):
    # logic of this funtion is store_app/views.py line 111
```
# Future prospects

Fix up the javascript code to be less primitive.  
Add few new html pages so that user interaction is more fluent.

## Links that may be usefull when reading the code
https://getbootstrap.com/  
https://getbootstrap.com/docs/4.0/components/navbar/#supported-content  
https://docs.djangoproject.com/en/4.2/howto/csrf/  
https://support.stripe.com/questions/how-to-fix-syntaxerror-unexpected-token-in-json-at-position-0  
https://stackoverflow.com/questions/987142/make-gitignore-ignore-everything-except-a-few-files  
https://stackoverflow.com/questions/17312831/what-does-request-user-refer-to-in-django  
https://stackoverflow.com/questions/3644902/how-to-check-if-a-user-is-logged-in-how-to-properly-use-user-is-authenticated  
https://stackoverflow.com/questions/10622199/how-to-retrieve-password-in-django  
https://stackoverflow.com/questions/3222549/how-to-automatically-login-a-user-after-registration-in-django  
https://stackoverflow.com/questions/25251719/how-can-i-logout-a-user-in-django  
https://stackoverflow.com/questions/4898408/how-to-set-a-login-cookie-in-django  
https://stackoverflow.com/questions/14503062/how-do-i-serve-a-text-file-from-django  
https://stackoverflow.com/questions/14639106/how-can-i-retrieve-a-list-of-field-for-all-objects-in-django  
https://stackoverflow.com/questions/431628/how-to-combine-multiple-querysets-in-django  
https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder  
https://stackoverflow.com/questions/24575680/new-lines-inside-paragraph-in-readme-md  
https://stackoverflow.com/questions/3828554/how-to-allow-input-type-file-to-accept-only-image-files  
https://blog.hubspot.com/website/opacity-css#:~:text=To%20set%20the%20opacity%20of,invisible).  
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select  
https://stackoverflow.com/questions/9129635/adding-an-image-from-a-url-html
