import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SellPurchase.models.farmer import Farmer
from django.contrib.auth.hashers import make_password
from django.views import View
from unicodedata import category
from SellPurchase.models.category import Category


class Signup(View):
    def get(self,request):
       return render(request,'signup.html')
    
    def post(self,request):
       postData=request.POST
       name=postData.get('name')
       address=postData.get('address')
       phone_no=postData.get('phone_no')
       email=postData.get('email')
       password=postData.get('password')
       password2=postData.get('pswd')
       if request.FILES:
            image=request.FILES['image']

       
       farmer=Farmer(name=name,address=address,
       phone_no=phone_no,email=email,password=password,image=image)
      
      
       # if email is already exist then none  
       try:
            is_email_exist = Farmer.objects.get(email=email)
       except Farmer.DoesNotExist:
            is_email_exist = None
       
       # created a fucntion  to validate user signup details
       error_message=self.validateFarmer(farmer,is_email_exist)



       if(password != password2):
          error_message="Password does not matches!!"

       value={
             'name':name,
             'address':address,
             'phone_no':phone_no,
             'email':email, 
             'image':image    
          }
 
      
       if not error_message:
           # hashing store password through hashing
           farmer.password=make_password(farmer.password)
           # save the farmer details
           farmer.save()
           return redirect('farmer_login')
       else:
           # otherwise show error on html 
           data={
                  'error':error_message,
                  'values':value
              }
           return render(request,'signup.html',data)

            

    def validateFarmer(self,farmer,is_email_exist):
        error_message=None
        if(not farmer.name):
           error_message="Name Required !!"
        elif len(farmer.name) < 4:
           error_message="Name is Too Short !!"
        elif(not farmer.address):
           error_message="address is Required !!"
        elif(not farmer.phone_no):
           error_message="Phone No. Required !!"
        elif(len(farmer.phone_no) != 10):
           error_message="Invalid Phone No !!"
        elif(not farmer.email):
           error_message="Email Required !!"
        elif(not farmer.password):
           error_message="Password Required !!"
        elif(len(farmer.password)<6):
           error_message="Password Must be 6 char Long"
        
        # if user is already exist then 
        elif(is_email_exist is not None):
           error_message="Email Already Registered ...!!"
        
        return error_message
