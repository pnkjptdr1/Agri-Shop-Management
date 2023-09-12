import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SellPurchase.models.product import Product
from SellPurchase.models.category import Category
from SellPurchase.models.farmer import Farmer
from django.views import View

from SellPurchase.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Products(View):
   
    @method_decorator(auth_middleware)
    def get(self,request):
       cart = request.session.get('cart')
       if not cart:
          request.session['cart']={}
       products=None
       categories=Category.get_all_categories();
       catagoryID=request.GET.get('category')
       if catagoryID:
           products=Product.get_all_products_by_category_id(catagoryID)
       else:
           products=Product.get_all_products();
       data={}
       data['products']=products
       data['categories']=categories
       return render(request,'product.html',data)
