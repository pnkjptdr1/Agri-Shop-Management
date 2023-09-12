from statistics import mode
from unicodedata import category
from django.db import models
from .category import Category


class Farmer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='uploads/products/',null=True,blank=True)
    
        
