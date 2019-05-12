from django.contrib import admin 
from .models import User,Material,Menu,Supplier,BuyMetProcess,MaterialItem
from viewflow.admin import ProcessAdmin
from . import models

class UserAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in User._meta.fields]
    fields = ('name', 'table_no', 'role')
admin.site.register(User, UserAdmin)

class MaterialAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Material._meta.fields]
    fields = ('user', 'name', 'quantity')

admin.site.register(Material, MaterialAdmin)

class MenuAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Menu._meta.fields]
    fields = ('user', 'name', 'description', 'price','image')

admin.site.register(Menu, MenuAdmin)

class SupplierAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Supplier._meta.fields]
    fields = ('material', 'name', 'location', 'telephone')

admin.site.register(Supplier, SupplierAdmin)

class MaterialItemAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Supplier._meta.fields]
    fields = ('material', 'name', 'quantity')

admin.site.register(MaterialItem, MaterialItemAdmin)

class BuyMetProcessAdmin(ProcessAdmin):
    icon = '<i class="material-icons">flag</i>'
    list_display = ['pk', 'created', 'status', 'participants',
                     'text']
    list_display_links = ['pk', 'created']


admin.site.register(models.BuyMetProcess, BuyMetProcessAdmin)
