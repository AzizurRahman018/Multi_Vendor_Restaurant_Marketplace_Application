from django import forms
from .models import User

class UserForm (forms.ModelForm):
    class meta:
        model=User
        fields = ['first_name', 'last_name','username','email','phone_number','password']