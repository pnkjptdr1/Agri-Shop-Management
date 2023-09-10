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
    
    def register(self):
        self.save()

    @staticmethod
    def get_farmer_by_email(email):
        try:
          return Farmer.objects.get(email=email)
        except:
            return False
            
    
    def isExists(self):
        if Farmer.objects.filter(email=self.email):
            return True
        
        return False