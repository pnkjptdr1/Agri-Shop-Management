from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.farmer import Farmer


# Register your models here.

admin.site.register(Product)
admin.site.register(Farmer)
admin.site.register(Category)


 

