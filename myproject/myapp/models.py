
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
        return '{} {}'.format(self.name, self.quantity)

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity']

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

    # class Meta:
    #     verbose_name_plural = 'Shipment process list'
    #     permissions = [
    #         ('can_start_request', 'Can start shipment request'),
    #         ('can_take_extra_insurance', 'Can take extra insurance'),
    #         ('can_package_goods', 'Can package goods'),
    #         ('can_move_package', 'Can move package')
    #     ]

    # def need_extra_insurance(self):
    #     try:
    #         return self.user.name
    #     except user.DoesNotExist:
    #         return None