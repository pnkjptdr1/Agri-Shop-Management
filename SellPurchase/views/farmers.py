from django.shortcuts import render,redirect
from SellPurchase.models.product import Product
from SellPurchase.models.category import Category
from SellPurchase.models.farmer import Farmer
from django.views import View



class Farmers(View):
   def post(self,request):
    product=request.POST.get('product')
    product=int(product)
    products=Product.get_product_by_id(product)
    return render(request,'farmers.html',{'products':products})
 


 