from typing import Any
from django import forms
from accounts.models import User

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields = ['first_name', 'last_name','username','email','phone_number','password']



   #non field error 
    def clean(self) :
        clean_data = super(UserForm , self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password Dose not Match !"

            )
