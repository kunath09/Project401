from django import forms
from django.forms import formset_factory

from material import *
from django.forms import ModelForm
from material.forms import ModelForm, InlineFormSetField,Form, FormSetField ,ModelFormField
from .models import Profile,Material,Menu,BuyMaterialProcess,MaterialItem,Restaurant,OrderMaterial
from django.template import Template
from django.forms import inlineformset_factory
from material import Layout, Row
from material.forms import AjaxModelSelect, get_ajax_suggestions

class MaterialForm(ModelForm):

    items = InlineFormSetField(
        OrderMaterial, MaterialItem,
        fields=['material', 'quantity'], can_delete=True)
    class Meta:
        model = OrderMaterial
        fields = ['restaurant','datestart']
        
        


    
        





    
