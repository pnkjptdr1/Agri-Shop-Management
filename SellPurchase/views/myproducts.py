from email.mime import image
from itertools import product
from django.shortcuts import render , redirect
from SellPurchase.models.farmer import Farmer
from SellPurchase.models.category import Category
from django.views import  View
from SellPurchase.models.product import  Product
from django.core.files.storage import FileSystemStorage
 
 

class Myproducts(View):
    def get(self ,request):
        farmer=request.session.get('farmer')
        products = Product.get_products_by_farmer(farmer)
        return render(request , 'myproducts.html' , {'products' : products} )


    def post(self ,request):
          product_id=request.POST.get('product')
          Product.delete_product_by_id(product_id)
          farmer=request.session.get('farmer')
          products = Product.get_products_by_farmer(farmer)
          return render(request , 'myproducts.html' , {'products' : products} )

           
         
   

     