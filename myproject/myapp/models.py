
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
    # stock = models.ForeignKey('Stock',on_delete = models.CASCADE,null=True,blank=True)
    # phone = models.DecimalField(max_digits = 15,decimal_places=0)

    def __str__(self):
        return self.name

class Stock(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True,blank=True)
    material = models.ForeignKey('Material',on_delete = models.PROTECT,null=True,blank=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,default=0,null=True,blank=True)
    # materialitem = models.ManyToManyField('MaterialItem')
    # matItem should null=true,blank=true
    # def save(self, *args, **kwargs):
    #     # totalobj = Stock.objects.count()
    #     temp =''
    #     for each in Stock.objects.all():
    #         if each.material == temp:
    #             add = each.quantity
    #             old = SumStock.objects.filter(material=temp)
    #         else:
    #             SumStock.objects.create(material=each.material,quantity=each.quantity)
    

    def __str__(self):
        # return '{} {} '.format(self.restaurant, self.materialitem)
        # return (f'{self.materialitem}')
        return '{} {} {} '.format(self.restaurant,self.material,self.quantity)

class SumStock(models.Model):
    stock = models.ForeignKey('Stock',on_delete = models.CASCADE)
    material = models.ForeignKey('Material',on_delete = models.PROTECT)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,default=0)

    def __str__(self):
        return '{} {} {} '.format(self.stock,self.material,self.quantity)


# @receiver(post_save, sender=Restaurant)
# def create_stock_profile(sender, instance, created, **kwargs):
#     if created:
#         Stock.objects.create(restaurant=instance)

# @receiver(post_save, sender=Restaurant)
# def save_stock_profile(sender, instance, **kwargs):
#     instance.stock.save()

    # def save(self, **kwargs):
    #     super(Stock, self).save(**kwargs)
    #     restaurant = Restaurant(stock=self)
    #     restaurant.save()
    
class Material(models.Model):
    name = models.CharField(max_length = 50,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

    def __str__(self):
        return '{}'.format(self.name)

class OrderMaterial(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
    # materialitem = models.ManyToManyField('MaterialItem',blank=True)
    # materialitems = models.ManyToManyField(Material,through='MaterialItem')
    datestart = models.DateField(auto_now_add=False,null=True)
    datesent = models.DateField(auto_now_add=False,null=True)
    datereturn = models.DateField(auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return ' {} / {}-{} / '.format(self.pk,self.restaurant,self.datestart)

class MaterialItem(models.Model):
    material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
    orderMaterial = models.ForeignKey('OrderMaterial', on_delete=models.CASCADE,null=True)
    # stock = models.ForeignKey('Stock', on_delete=models.CASCADE,null=True)
    quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)
    # note = models.CharField(max_length = 50,blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.material, self.quantity,self.orderMaterial.restaurant)
        # self.orderMaterial.restaurant

# class Material(models.Model):
#     name = models.CharField(max_length = 50,null=True)
#     quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)

#     def __str__(self):
#         return '{} {} '.format(self.name, self.quantity)

# class MaterialItem(models.Model):
#     material = models.ForeignKey('Material',on_delete = models.CASCADE,null=True)
#     quantity = models.DecimalField(max_digits=8,decimal_places=0,null=True)
#     date = models.DateField(auto_now_add=False,null=True)

#     def __str__(self):
#         return '{} {}'.format(self.material, self.quantity)

class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.name
# อาจจะต้องใช้ through
class OrderMenu(models.Model):
    restaurant = models.ForeignKey('Restaurant',on_delete = models.CASCADE,null=True)
    menuitem = models.ManyToManyField('MenuItem')
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
    ordermaterial = models.ForeignKey('OrderMaterial',blank=True, null=True, on_delete=models.CASCADE)
    # materialitem = models.ForeignKey('MaterialItem',blank=True ,null=True, on_delete=models.CASCADE)
    # restaurant = models.ManyToManyField('Restaurant')
    text = models.CharField(max_length=100,blank=True)
    # num = models.IntegerField(null=True)
    approved = models.BooleanField(default=False)
