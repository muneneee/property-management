from django import forms
from .models import Tenant, House, Property

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'contact_info', 'house']
        widgets = {
            'house': forms.Select(attrs={'class': 'form-control'})
        }

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['property', 'house_rent', 'deposit']
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'})
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('client_details', 'property_address')

class InvoiceForm(forms.Form):
    rent = forms.DecimalField(label='Rent', max_digits=8, decimal_places=2)
    garbage_service = forms.DecimalField(label='Garbage Service', max_digits=8, decimal_places=2)