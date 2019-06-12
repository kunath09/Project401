from rest_framework import serializers
from myapp.models import Profile,Material,Menu,Stock,MenuItem,OrderMenu,Restaurant,OrderMaterial,MaterialItem
from django.contrib.auth.models import User
from django.db.models import Count,Sum

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('pk','name', 'address','phone')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'restaurant', 'role','phone')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('pk','name', 'quantity')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('pk','restaurant', 'material', 'quantity')
        

    def to_representation(self, instance):
        self.fields['restaurant'] =  RestaurantSerializer(read_only=True)
        self.fields['material'] =  MaterialSerializer(read_only=True)
        return super(StockSerializer, self).to_representation(instance)

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
        fields = ('pk','restaurant', 'name', 'description','price','image')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('pk','orderMenu','menu','quantity')

class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = ('pk','date',)

