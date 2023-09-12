from django.shortcuts import render,redirect,HttpResponseRedirect
from SellPurchase.models.product import Product
from SellPurchase.models.category import Category
from SellPurchase.models.farmer import Farmer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'farmer_login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
       
        # Retrieve a single Farmer object using get() instead of filter()
        try:
            farmer = Farmer.objects.get(email=email)
        except Farmer.DoesNotExist:
            farmer = None

        
        error_message = None

        if farmer is not None:
            flag = check_password(password,farmer.password)
            if flag:

                # store data in the session 
                request.session['farmer']=farmer.id
                
                if Login.return_url:
                   # agar nhi huva to usi page per waps for refresh
                   return HttpResponseRedirect(Login.return_url)
                else:
                   # agar login ho gya to
                   Login.return_url=None
                   return redirect('index')
            else:
                error_message = 'Email or Password Invalid ...!!'
        else:
            error_message = 'Email or Password Invalid ...!!'
        return render(request,'farmer_login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('index')
