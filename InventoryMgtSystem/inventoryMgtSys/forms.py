from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Password must contain at least one digit.')
        return password2


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        print(f"Username: {username}")
        print(f"Password: {password}")

        if username and password:
            # Authenticate user
            user = authenticate(request=self.request, username=username, password=password)

            print(f"Authenticated User: {user}")

            # Check if authentication was successful
            if user is not None:
                print("User is authenticated")
            else:
                print("User authentication failed")

        return self.cleaned_data


class CounterPartyForm(forms.ModelForm):
    class Meta:
        model = CounterParty
        fields = '__all__'
        exclude = ['active']


class InventoryForm(forms.ModelForm):
   class Meta:
       model = Inventory
       fields = '__all__'


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add widgets for the booking date and shipment date fields
        self.fields['booking_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['shipment_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})


class ExpenseForm(forms.ModelForm):
   class Meta:
       model = Expense
       fields = '__all__'


class IncomeForm(forms.ModelForm):
   class Meta:
       model = Income
       fields = '__all__'