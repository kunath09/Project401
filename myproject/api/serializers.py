from rest_framework import serializers
from myapp.models import Profile,Material,Menu
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'restaurant', 'role','phone')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('user', 'quantity')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('restaurant', 'name', 'description','price','image')

# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Supplier
#         fields = ('material', 'name', 'location','telephone')