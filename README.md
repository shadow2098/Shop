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
<img width="1440" alt="admin" src="https://github.com/shadow2098/Shop/assets/93429735/21c1159a-85a4-435e-a55b-f0cfa1ab2cd2">
And fill out the form for the product creation.    
  
2) You can also add products by creating seller account. ***Note: Log out as a superuser in the admin panel before entering http://127.0.0.1:8000/***  
***Important note: If you plan to add products this way, you will NOT be able to see images attached to the products***
