from rest_framework import serializers
from myapp.models import Profile,Material,Menu,Stock,MenuItem,OrderMenu
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'restaurant', 'role','phone')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name', 'quantity')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('restaurant', 'name', 'description','price','image')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('restaurant', 'materialitem')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('menu','quantity')

class OrderMenuSerializer(serializers.ModelSerializer):
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