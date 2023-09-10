from django.contrib import admin
from django.urls import path
from SellPurchase.views.old import *
from django.conf import settings
from django.conf.urls.static import static
from SellPurchase.views import farmers, signup,farmer_login,index,addproduct,product,myproducts



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index.index, name='index'),

    path('products', product.Products.as_view(), name='product'),
    path('addproduct', addproduct.Addproduct.as_view(), name='addproduct'),
    path('farmer_login',farmer_login.Login.as_view(), name='farmer_login'),
    path('logout/',farmer_login.logout,name='logout'),
    path('signup',signup.Signup.as_view(),name='signup'),

    path('farmer_contact',farmers.Farmers.as_view(),name='farmer_contact'),
    path('myproducts', myproducts.Myproducts.as_view() ,name='myproducts'),


    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('addcategory', addcategory, name='addcategory'),
    path('managecategory', managecategory, name='managecategory'),
    path('editcategory<int:pid>', editcategory, name='editcategory'),
    path('deletecategory<int:pid>', deletecategory, name='deletecategory'),



    path('regfarmers', regfarmers, name='regfarmers'),
    path('deletefarmer<int:pid>', deletefarmer, name='deletefarmer'),
    path('listedproducts', listedproducts, name='listedproducts'),
    path('deleteproduct<int:pid>', deleteproduct, name='deleteproduct'),


   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
