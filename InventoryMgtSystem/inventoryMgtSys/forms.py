from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # Add your custom password validation logic here
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Password must contain at least one digit.')
        # ... add more validation rules as needed
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



# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CounterPartyForm(forms.ModelForm):
    class Meta:
        model = CounterParty
        fields = ['name', 'email', 'contact_person', 'active', 'address_line1', 'city', 'state']