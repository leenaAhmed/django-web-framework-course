from django.db import models
from datetime import datetime
# Create your models here.



class Product(models.Model):

    categoryList = [
        ('phone' , 'Phone'),
    ]
    name = models.CharField(max_length=50 , verbose_name='Product Name')
    price = models.DecimalField(max_digits= 5 ,decimal_places =2)
    contact = models.TextField(null=True,blank=True ,  verbose_name='Product Discription')
    image = models.ImageField(upload_to="photos/%y/%m/%d", default='photos/24/12/01/camera-icon-png-8.jpg')
    active= models.BooleanField(default=True)
    category= models.CharField(max_length=255 , null=True, blank=True ,choices= categoryList)
    def __str__(self):
        return self.name;
    
    class Meta:
        verbose_name = 'App product'
        ordering = ['price']


class Category(models.Model):
    date = models.DateField()
    time = models.TimeField(null= True, blank=True)
    name = models.CharField(max_length=55)
    created = models.DateTimeField(null= True, blank=True , default=datetime.now)

    def __str__(self):
        return self.name;


