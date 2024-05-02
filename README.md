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
Note: You can use pictures from store_app/static/store_app/images/ for test products  
1) Enter http://127.0.0.1:8000/admin/ , enter your superuser info, and click the same button as in the image below
<img width="1440" alt="admin" src="https://github.com/shadow2098/Shop/assets/93429735/21c1159a-85a4-435e-a55b-f0cfa1ab2cd2">
And fill out the form for the product creation.    
  
2) You can also add products by creating seller account. ***Note: Log out as a superuser in the admin panel before entering http://127.0.0.1:8000/***  
***Important note: If you plan to add products this way, you will NOT be able to see images attached to the products***

Click "Log in" in the up right corner of the http://127.0.0.1:8000/ -> Click "Log in as seller" -> Click sign up as seller. After that go to http://127.0.0.1:8000/add_product/ and fill out the form. You should be able to see you product apprear in the catalog on main page **AS it was said, this way you and other users cannot see product images**


# Coursework requirements

### Abstraction and Inheritance
store_app/models.py line 5 is abstract class, and then Guest, Customer, Seller, and Product are children of abstarct class

### Encapsulation
store_app/models.py Guest, Customer, and Seller classes have _ (protected) fields, and by default fields are also private inside django models

### Polymorphism and writing to file
store_app/views.py line 56 is a function where we treat Guest, Customer, and Seller objects as same type and write all usernames into the file

### Decorator
Different decorators are used throughout store_app/views.py

# Future prospects
Fix the issue that picture is not visible when seller uploads the product.  
Fix up the javascript code to be less primitive.  
Add few new html pages so that user interaction is more fluent.

## Links that may be usefull when reading the code
https://getbootstrap.com/
https://getbootstrap.com/docs/4.0/components/navbar/#supported-content
https://github.com/divanov11/ecom_steps/blob/master/prt6_stp3_main.html
@property - makes a method be accessible as an attribute
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
