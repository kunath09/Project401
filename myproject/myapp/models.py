
from __future__ import unicode_literals
from django.db import models
from viewflow.models import Process,Task
from django.forms import ModelForm


from django.utils.encoding import python_2_unicode_compatible

# USER_ROLE= (
#         ('Che', 'Chef'),
#         ('Man','Manager'),
#         ('Cus','Customer'),
#     )
    
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     table_no = models.CharField(max_length=100)
#     role = models.CharField(
#         max_length=10,
#         choices=USER_ROLE,
#         default='Che',
#     )
#     def __str__(self):
#         return self.name

# class Material(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     quantity = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         # return '{} {}'.format(self.name, self.quantity)
#         return self.name

# class MaterialItem(models.Model):
#     material = models.ForeignKey('Material', on_delete=models.CASCADE, default='')
#     name = models.CharField(max_length=100, default='test')
#     quantity = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return self.name


# class Menu(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=100,)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     image = models.ImageField(upload_to='media')

#     def __str__(self):
#         return self.name

# class Supplier(models.Model):
#     material = models.ForeignKey('Material', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name


# class BuyMetProcess(Process):
#     material = models.ForeignKey('Material',blank=True, null=True, on_delete=models.CASCADE)
#     # material = models.ManyToManyField('Material')
#     text = models.CharField(max_length=100)
#     num = models.IntegerField(null=True)
#     approved = models.BooleanField(default=False)

 #########################################

from django.contrib.auth.models import User
from datetime import date,datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

USER_ROLE= (
        ('Che', 'Chef'),
        ('Man','Manager'),
        ('Sup','Supplier'),
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLE,
        default='Che',
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return '{} {}'.format(self.user, self.restaurant)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Restaurant(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # phone = models.DecimalField(max_digits = 15,decimal_places=0)

    def __str__(self):
        return self.name

class Stock(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE)
    materialitem = models.ForeignKey('MaterialItem',on_delete = models.CASCADE)

    def __str__(self):
        return '{} {} '.format(self.restaurant, self.materialitem)

# class Material(models.Model):
#     name = models.CharField(max_length = 50,null=True)
#     quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

#     def __str__(self):
#         return '{} {} '.format(self.name, self.quantity)

# class OrderMaterial(models.Model):
#     restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
#     # material = models.ManyToManyField('Material',through='MaterialItem',blank=True)
#     material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
#     datestart = models.DateField(auto_now_add=False,null=True)
#     datesent = models.DateField(auto_now_add=False,null=True)
    
#     def __str__(self):
#         return '{} {} {} {} '.format(self.restaurant,self.material,self.datestart,self.datesent)

# class MaterialItem(models.Model):
#     material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
#     orderMaterial = models.ForeignKey('OrderMaterial', on_delete=models.CASCADE,null=True)
#     quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

#     def __str__(self):
#         return '{} {}'.format(self.material, self.quantity)

class Material(models.Model):
    name = models.CharField(max_length = 50,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

    def __str__(self):
        return '{} {} '.format(self.name, self.quantity)

class MaterialItem(models.Model):
    material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)
    date = models.DateField(auto_now_add=False,null=True)

    def __str__(self):
        return '{} {}'.format(self.material, self.quantity)

class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.name

class OrderMenu(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
    menuitem = models.ManyToManyField('MenuItem',null=True)
    date = models.DateField(auto_now_add=False,null=True)
    success = models.BooleanField(default=False,null=True)
    
    def __str__(self):
        return '{} {} {} {} '.format(self.restaurant,self.menuitem,self.date,self.success)

class MenuItem(models.Model):
    menu = models.ForeignKey('Menu',on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits=8,decimal_places=0)

    def __str__(self):
        return '{} {} '.format(self.menu, self.quantity)

# class BuyMaterialProcess(Process):
#     orderMaterial = models.ForeignKey('OrderMaterial',blank=True, null=True, on_delete=models.CASCADE)
#     # restaurant = models.ManyToManyField('Restaurant')
#     text = models.CharField(max_length=100)
#     num = models.IntegerField(null=True)
#     approved = models.BooleanField(default=False)


class BuyMaterialProcess(Process):
    material = models.ForeignKey('Material',blank=True, null=True, on_delete=models.CASCADE)
    # restaurant = models.ManyToManyField('Restaurant')
    text = models.CharField(max_length=100)
    num = models.IntegerField(null=True)
    approved = models.BooleanField(default=False)