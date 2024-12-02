from django.db import models

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
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True) #one to many
    gender= models.CharField(max_length=255 , null=True, blank=True ,choices= categoryList)

    def __str__(self):
        return self.name


