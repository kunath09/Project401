
from __future__ import unicode_literals
from django.db import models
from viewflow.models import Process,Task
from django.forms import ModelForm


from django.utils.encoding import python_2_unicode_compatible

USER_ROLE= (
        ('Che', 'Chef'),
        ('Man','Manager'),
        ('Cus','Customer'),
    )
    
class User(models.Model):
    name = models.CharField(max_length=100)
    table_no = models.CharField(max_length=100)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLE,
        default='Che',
    )
    def __str__(self):
        return self.name

class Material(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        # return '{} {}'.format(self.name, self.quantity)
        return self.name

class MaterialItem(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, default='test')
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Menu(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class BuyMetProcess(Process):
    material = models.ForeignKey('Material',blank=True, null=True, on_delete=models.CASCADE)
    # material = models.ManyToManyField('Material')
    text = models.CharField(max_length=100)
    num = models.IntegerField(null=True)
    approved = models.BooleanField(default=False)

 #########################################

# from django.contrib.auth.models import User

# USER_ROLE= (
#         ('Che', 'Chef'),
#         ('Man','Manager'),
#         ('Sup','Supplier'),
#     )

# class Users(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     resturant = models.ForeignKey('Resturant',on_delete = models.CASCADE)
#     role = models.CharField(
#         max_length=10,
#         choices=USER_ROLE,
#         default='Che',
#     )
#     phone = models.DecimalField(max_digits=15)

#     def __str__(self):
#         return self.name

# class Resturant(models.Model):
#     name = models.CharField(max_length = 50)
#     address = models.CharField(max_length = 100)
#     phone = models.DecimalField(max_digits = 15)

#     def __str__(self):
#         return self.name

# class Material(models.Model):
#     name = models.CharField(max_length = 50)

#     def __str__(self):
#         return self.name

# class MaterialItem(models.Model):
#     material = models.ForeignKey('Material',on_delete = models.CASCADE,default = '')
#     quantity = models.DecimalField(max_digits=8)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class Menu(models.Model):
#     resturant = models.ForeignKey('Resturant',on_delete = models.CASCADE)
#     name = models.CharField(max_length = 50)
#     description = models.CharField(max_length = 100)
#     price = models.DecimalField(max_digits=10,decimal_places=2)
#     image = models.ImageField(upload_to = 'media')

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     menu = models.ForeignKey('Menu',on_delete = models.CASCADE,default = '')
#     date = models.DateField(auto_now_add=True)
#     quantity = models.DecimalField(max_digits=8)
#     success = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

# class BuyMaterialProcess(Process):
#     material = models.ForeignKey('Material',blank=True, null=True, on_delete=models.CASCADE)
#     text = models.CharField(max_length=100)
#     num = models.IntegerField(null=True)
#     approved = models.BooleanField(default=False)
