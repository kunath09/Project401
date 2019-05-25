from rest_framework import serializers
from myapp.models import Profile,Material,Menu
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

# class BuyMaterialProcessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ('restaurant', 'approved')

# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Supplier
#         fields = ('material', 'name', 'location','telephone')