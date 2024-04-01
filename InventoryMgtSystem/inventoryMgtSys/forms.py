from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['admin', 'active']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)