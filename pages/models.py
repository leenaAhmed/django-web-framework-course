from django.db import models
from django.views import View 
from django.http import HttpResponse
# Create your models here.


class UserId(models.Model):
    user_Id = models.CharField(max_length=15)
    def __str__(self):
        return self.user_Id
    
class Department(models.Model):
    name =  models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.name
    
class User(models.Model):
    categoryList = [
        ('male' , 'Male'),
        ('female' , 'Female'),
    ]

    name = models.CharField(max_length=15, verbose_name='User Name')
    cardId = models.OneToOneField(
        UserId, 
        on_delete=models.PROTECT,  # or SET_NULL, CASCADE based on your use case
        verbose_name="card Id")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True , related_name="department") #one to many
    gender= models.CharField(max_length=255 , null=True, blank=True ,choices= categoryList)
    tax_code = models.CharField( max_length = 20,unique = True , null=True, blank=True) 
    grade = models.DecimalField( 
                         max_digits = 5, 
                         null=True,
                         decimal_places = 2) 
    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=20,  null=True)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name

class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 