from django import forms
from vendor.models import  Vendor

class VendorForm(forms.ModelForm):
     
     class Meta:
        model=Vendor        
        fields = ['vendor_license', 'vendor_name']











