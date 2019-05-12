from django import forms
from django.forms import formset_factory

from material import *
from django.forms import ModelForm
from material.forms import ModelForm, InlineFormSetField,Form, FormSetField ,ModelFormField
from .models import User,Material,Menu,Supplier,BuyMetProcess,MaterialItem
from django.template import Template
from django.forms import inlineformset_factory
from material import Layout, Row
from material.forms import AjaxModelSelect, get_ajax_suggestions

# class MaterialForm(forms.ModelForm):
#     class Meta:
#         model = Material
#         fields = ['user','name', 'quantity']

# MaterialFormSet = formset_factory(MaterialForm, extra=3, can_delete=True) 

# class OrderForm(Form):
#     materials = FormSetField(formset_class=MaterialFormSet)

class MaterialForm(ModelForm):
    # ModelForm

    class Meta:
        model = Material
        
        fields = [
            'name',
            #should be resturant
        ]
        # widgets = {
        #     'material': AjaxModelSelect(lookups=['name__icontains'])
        # }

    # items = InlineFormSetField(
    #     Material, MaterialItem,
    #     fields=['material', 'quantity'], can_delete=True,extra=1)

# MaterialFormSet = formset_factory(MaterialForm, extra=1, can_delete=True)
    class OrderForm(ModelForm):
        class Meta:
            model = MaterialItem
            fields = ('material','quantity')

    OrderFormSet = forms.formset_factory(
        OrderForm, extra=1, can_delete=True)

    Orders = FormSetField(OrderFormSet)

    

# class FinalForm(Form):

#     order = FormSetField(formset_class=MaterialFormSet)

#     layout = Layout(
#         'order'
#     )


    



    
