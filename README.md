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
