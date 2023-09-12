from email.mime import image
from itertools import product
from django.shortcuts import render , redirect
from SellPurchase.models.farmer import Farmer
from SellPurchase.models.category import Category
from django.views import  View
from SellPurchase.models.product import  Product
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# for session handling to check user already login or not
from SellPurchase.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
 

class Myproducts(View):
    # method_decorator check if user is login or not if not login then send it to login page
    @method_decorator(auth_middleware)
    def get(self ,request):
        farmer=request.session.get('farmer')
        products = Product.get_products_by_farmer(farmer)
        return render(request , 'myproducts.html' , {'products' : products} )

    # @login_required(login_url ='farmer_login')
    def post(self ,request):
          product_id=request.POST.get('product')
          Product.delete_product_by_id(product_id)
          farmer=request.session.get('farmer')
          products = Product.get_products_by_farmer(farmer)
          return render(request , 'myproducts.html' , {'products' : products} )

           
         
   

     
