from django import forms
from django.forms import formset_factory
# from material.forms import Form
from material import *
from django.forms import ModelForm
# from material.forms import ModelForm, InlineFormSetField
from .models import User,Material,Menu,Supplier,BuyMetProcess
from django.template import Template
from django.forms import inlineformset_factory

# class CreatOrderForm(forms.Form):

    
#     # user = forms.CharField()
#     name = forms.CharField()
    # quantity = forms.CharField()

    # class Meta:
    #     model = Material
    #     fields = [
    #         'name', 'quantity'
    #     ]
    
    
    # layout = Layout('material', 'quantity')


    # username = forms.CharField()
    # email = forms.EmailField(label="Email Address")
    # password = forms.CharField(widget=forms.PasswordInput)
    # password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)
    # gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    # receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
    # agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    # layout = Layout('username', 'email',
    #                 Row('password', 'password_confirm'),
    #                 Fieldset('Personal details',
    #                          Row('first_name', 'last_name'),
    #                          'gender', 'receive_news', 'agree_toc'))
class CreatOrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    quantity = forms.DecimalField(max_digits=5, decimal_places=2)

# InlineFormSet = inlineformset_factory(Material, Supplier,fields=('name',))
# material = Material.objects.get(name='pork')
# formset = Supplier_Set(instance=material)