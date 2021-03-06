from django.contrib import admin 
from .models import Profile,Material,Menu,BuyMaterialProcess,MaterialItem,Restaurant,OrderMenu,Stock,MenuItem,OrderMaterial,ManageMenuProcess
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
    list_display  = [f.name for f in Profile._meta.fields]
 
admin.site.register(Profile, ProfileAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Restaurant._meta.fields]


admin.site.register(Restaurant, RestaurantAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Stock._meta.fields]

admin.site.register(Stock, StockAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Material._meta.fields]

admin.site.register(Material, MaterialAdmin)

class OrderMaterialAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in OrderMaterial._meta.fields]

admin.site.register(OrderMaterial, OrderMaterialAdmin)

class MaterialItemAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in MaterialItem._meta.fields]
    list_filter = (
        ('orderMaterial', admin.RelatedOnlyFieldListFilter),
    )

admin.site.register(MaterialItem, MaterialItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Menu._meta.fields]

admin.site.register(Menu, MenuAdmin)

class OrderMenuAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in OrderMenu._meta.fields]

admin.site.register(OrderMenu, OrderMenuAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in MenuItem._meta.fields]
 
admin.site.register(MenuItem, MenuItemAdmin)

class BuyMaterialProcessAdmin(ProcessAdmin):
    icon = '<i class="material-icons">flag</i>'
    list_display = ['pk', 'created', 'status', 'participants'
                     ]
    list_display_links = ['pk', 'created']

admin.site.register(models.BuyMaterialProcess, BuyMaterialProcessAdmin)

class ManageOrderProcessAdmin(ProcessAdmin):
    icon = '<i class="material-icons">flag</i>'
    list_display = ['pk', 'created', 'status', 'participants'
                     ]
    list_display_links = ['pk', 'created']

admin.site.register(models.ManageOrderProcess, ManageOrderProcessAdmin)

class ManageMenuProcessAdmin(ProcessAdmin):
    icon = '<i class="material-icons">flag</i>'
    list_display = ['pk', 'created', 'status', 'participants'
                     ]
    list_display_links = ['pk', 'created']

admin.site.register(models.ManageMenuProcess, ManageMenuProcessAdmin)

