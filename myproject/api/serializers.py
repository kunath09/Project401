from rest_framework import serializers
from myapp.models import User,Material,Menu,Supplier
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'table_no', 'role')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('user', 'name', 'quantity')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('user', 'name', 'description','price','image')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('material', 'name', 'location','telephone')