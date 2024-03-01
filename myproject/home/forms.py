from django import forms
class FormName(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    mobile=forms.CharField(max_length=15)
    address=forms.CharField(max_length=100)
    place=forms.CharField(max_length=100)
                           
    
    