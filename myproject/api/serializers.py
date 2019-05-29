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
    # restaurant = RestaurantSerializer(read_only=True)
    # material = MaterialSerializer(read_only=True)
    # total_item = serializers.IntegerField()
    # total_capacity = serializers.IntegerField()
    # total = serializers.IntegerField()
    
    class Meta:
        model = Stock
        fields = ('pk','restaurant', 'material', 'quantity')
        # fields = '__all__'

    def to_representation(self, instance):
        self.fields['restaurant'] =  RestaurantSerializer(read_only=True)
        self.fields['material'] =  MaterialSerializer(read_only=True)
        return super(StockSerializer, self).to_representation(instance)
    # def get_total_item(self, obj):
    #     totalitem = Stock.objects.all().aggregate(total_item=Count('material'))
    #     return totalitem["total_item"]
    # def get_total_capacity(self, obj):
    #     totalcapacity = Stock.objects.all().aggregate(total_capacity=Sum('quantity'))
    #     return totalcapacity["total_capacity"]
    # def get_total_item_count(self, obj):
    #     return obj.total_item_set.count()

# class SumStockSerializer(serializers.ModelSerializer):
#     # stock = StockSerializer(read_only=True)
#     # material = MaterialSerializer(read_only=True)
#     class Meta:
#         model = SumStock
#         fields = ('stock', 'material', 'quantity')

#     def to_representation(self, instance):
#         self.fields['stock'] =  StockSerializer(read_only=True)
#         self.fields['material'] =  MaterialSerializer(read_only=True)
#         return super(SumStockSerializer, self).to_representation(instance)

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
# แกเรื่องคืน pk กับ def_torepresent
class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Menu
        fields = ('pk','restaurant', 'name', 'description','price','image')

class MenuItemSerializer(serializers.ModelSerializer):
    # menu = MenuSerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ('orderMenu','menu','quantity')

class OrderMenuSerializer(serializers.ModelSerializer):
    # restaurant = RestaurantSerializer(read_only=True)
    # menuItem = MenuItemSerializer(read_only=True)
    class Meta:
        model = OrderMenu
        fields = ('date',)




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