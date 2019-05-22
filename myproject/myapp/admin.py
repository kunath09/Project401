from django.contrib import admin 
from .models import Profile,Material,Menu,BuyMaterialProcess,MaterialItem,Restaurant,OrderMenu,Stock,MenuItem
from viewflow.admin import ProcessAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . import models

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in User._meta.fields]
    fields = ('user', 'restaurant','role','phone',)
admin.site.register(Profile, ProfileAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Supplier._meta.fields]
    fields = ('name', 'address','phone',)

admin.site.register(Restaurant, RestaurantAdmin)

class StockAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in User._meta.fields]
    fields = ('restaurant','materialitem',)
admin.site.register(Stock, StockAdmin)

class MaterialAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Material._meta.fields]
    fields = ('name','quantity',)

admin.site.register(Material, MaterialAdmin)

# class OrderMaterialAdmin(admin.ModelAdmin):
#     # list_display  = [f.name for f in Material._meta.fields]
#     fields = ('restaurant','materialitem','datestart','datesent')

# admin.site.register(OrderMaterial, OrderMaterialAdmin)

class MaterialItemAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Supplier._meta.fields]
    fields = ('material', 'quantity','date',)

admin.site.register(MaterialItem, MaterialItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Menu._meta.fields]
    fields = ('restaurant', 'name', 'description', 'price','image',)

admin.site.register(Menu, MenuAdmin)

class OrderMenuAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Menu._meta.fields]
    fields = ('restaurant', 'menuitem', 'date', 'seccess', )

admin.site.register(OrderMenu, OrderMenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    # list_display  = [f.name for f in Supplier._meta.fields]
    fields = ('menu', 'quantity', )

admin.site.register(MenuItem, MenuItemAdmin)

class BuyMaterialProcessAdmin(ProcessAdmin):
    icon = '<i class="material-icons">flag</i>'
    list_display = ['pk', 'created', 'status', 'participants',
                     'text']
    list_display_links = ['pk', 'created']

admin.site.register(models.BuyMaterialProcess, BuyMaterialProcessAdmin)
