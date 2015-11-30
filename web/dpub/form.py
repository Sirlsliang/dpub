from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(label='YourName',max_length=100)
    
