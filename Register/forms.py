from django import forms 
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['Name', 'Email', 'Age', 'PhoneNum','Designation', 'Photo']
