from rest_framework import serializers
from myapp.models import Profile,Material,Menu,Stock,MenuItem,OrderMenu,Restaurant,OrderMaterial,SumStock,MaterialItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address','phone')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'restaurant', 'role','phone')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name', 'quantity')

class StockSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    class Meta:
        model = Stock
        fields = ('restaurant', 'material', 'quantity')

class SumStockSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    class Meta:
        model = SumStock
        fields = ('stock', 'material', 'quantity')

class OrderMaterialSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = OrderMaterial
        fields = ('restaurant', 'datestart','datesent','datereturn')

class MaterialItemSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    orderMaterial = OrderMaterialSerializer(read_only=True)
    class Meta:
        model = MaterialItem
        fields = ('material', 'orderMaterial','quantity')

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Menu
        fields = ('restaurant', 'name', 'description','price','image')

class MenuItemSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ('menu','quantity')

class OrderMenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    menuItem = MenuItemSerializer(read_only=True)
    class Meta:
        model = OrderMenu
        fields = ('restaurant', 'menuitem', 'date','success')




# class BuyMaterialProcessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ('restaurant', 'approved')

# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Supplier
#         fields = ('material', 'name', 'location','telephone')
#  



# add stock menu ordermenu menuitem 