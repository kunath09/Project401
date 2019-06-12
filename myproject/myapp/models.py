
from __future__ import unicode_literals
from django.db import models
from viewflow.models import Process,Task
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
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
#set permission role at django admin

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

    def __str__(self):
        return self.name

class Stock(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True,blank=True)
    material = models.ForeignKey('Material',on_delete = models.PROTECT,null=True,blank=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,default=0,null=True,blank=True)

    def __str__(self):
        return '{} {} {} '.format(self.restaurant,self.material,self.quantity)
    
class Material(models.Model):
    name = models.CharField(max_length = 50,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

    def __str__(self):
        return '{}'.format(self.name)

class OrderMaterial(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
    datestart = models.DateField(auto_now_add=False,null=True)
    datesent = models.DateField(auto_now_add=False,null=True)
    datereturn = models.DateField(auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return ' {} / {}-{} / '.format(self.pk,self.restaurant,self.datestart)

class MaterialItem(models.Model):
    material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
    orderMaterial = models.ForeignKey('OrderMaterial', on_delete=models.CASCADE,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

    def __str__(self):
        return '{} {} {}'.format(self.material, self.quantity,self.orderMaterial.restaurant)

class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = 'media')

    def __str__(self):
        return '{} '.format(self.name)

class OrderMenu(models.Model):
    date = models.DateField(auto_now_add=False,null=True)
    
    def __str__(self):
        return '{} {} '.format(self.pk,self.date)

class MenuItem(models.Model):
    orderMenu = models.ForeignKey('OrderMenu',on_delete = models.CASCADE,null=True)
    menu = models.ForeignKey('Menu',on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits=8,decimal_places=0)

    def __str__(self):
        return '{} {} {}'.format(self.pk,self.menu, self.quantity)

class BuyMaterialProcess(Process):
    ordermaterial = models.ForeignKey('OrderMaterial',blank=True, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=100,blank=True)
    approved = models.BooleanField(default=False)


class BuyMaterialTask(Task):
    class Meta:
        proxy = True
    
class ManageOrderProcess(Process):
    menuitem = models.ForeignKey('MenuItem',on_delete = models.CASCADE,null=True,blank=True)
    cook = models.DateTimeField(auto_now_add=False,null=True)
    serve = models.DateTimeField(auto_now_add=False,null=True)
    pay = models.DateTimeField(auto_now_add=False,null=True)
    returnitem = models.BooleanField(default=False)

class ManageMenuProcess(Process):
    menu = models.ForeignKey('Menu',on_delete = models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=False,null=True)

