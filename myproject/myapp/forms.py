from django import forms
from django.forms import formset_factory

from material import *
from django.forms import ModelForm
from material.forms import ModelForm, InlineFormSetField,Form, FormSetField ,ModelFormField
from .models import Profile,Material,Menu,BuyMaterialProcess,MaterialItem,Restaurant
from django.template import Template
from django.forms import inlineformset_factory
from material import Layout, Row
from material.forms import AjaxModelSelect, get_ajax_suggestions



class RestaurantForm(ModelForm):
    class Meta:
        model = Material
        fields = ['name']

class MaterialForm(ModelForm):
    
    class OrderForm(ModelForm):
        class Meta:
            model = MaterialItem
            fields = ('material','quantity')

    OrderFormSet = forms.formset_factory(
        OrderForm, extra=3, can_delete=True)

    Orders = FormSetField(OrderFormSet)
    

    # items = InlineFormSetField(
    #     Material, MaterialItem,
    #     fields=['material', 'quantity'], can_delete=False)

    class Meta:
        model = Material
        
        fields = [
            'name',
        ]
        





    
