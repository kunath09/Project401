from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from myapp.models import Profile,Material,Menu,Stock,MenuItem,OrderMenu
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import ProfileSerializer,MaterialSerializer,MenuSerializer,StockSerializer,MenuItemSerializer,OrderMenuSerializer
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated,)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (IsAuthenticated,)

class OrderMenuViewSet(viewsets.ModelViewSet):
    queryset = OrderMenu.objects.all()
    serializer_class = OrderMenuSerializer
    permission_classes = (IsAuthenticated,)

# class BuyMaterialProcessViewSet(viewsets.ModelViewSet):
#     queryset = BuyMaterialProcess.objects.all()
#     serializer_class = BuyMaterialProcessSerializer
#     permission_classes = (IsAuthenticated,)

# class SupplierViewSet(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = (IsAuthenticated,)

    