import os
from pyexpat.errors import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from passlib.hash import pbkdf2_sha256
from django.contrib import messages
from hashlib import pbkdf2_hmac
import base64

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dash(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after registration
        else:
            # Handle invalid form data with error messages
            for error in form.errors:
                messages.error(request, error)  # Add error messages for popups
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)
                return redirect('dashboard')  # Redirect to homepage after login
            else:
                print("User authentication failed")
                # Handle invalid credentials
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user_login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout





def UserRetrieveUpdateDestroy(request, pk):
    return render(request, 'user_detail.html')

def CounterPartyListCreate(request):
    # Retrieve all counterparties
    counterparties = CounterParty.objects.all()
    data = {'counterparties': list(counterparties.values())}
    return JsonResponse(data)

def CounterPartyRetrieveUpdateDestroy(request, pk):
    try:
        # Retrieve the specific counterparty
        counterparty = CounterParty.objects.get(pk=pk)
        data = {'counterparty': counterparty}
        return JsonResponse(data)
    except CounterParty.DoesNotExist:
        return JsonResponse({'error': 'CounterParty not found'}, status=404)

def InventoryListCreate(request):
    return render(request, 'templates/inventory_list_create.html')

def InventoryRetrieveUpdateDestroy(request, pk):
    return render(request, 'templates/inventory_detail.html')

def DealListCreate(request):
    return render(request, 'templates/deal_list_create.html')

def DealRetrieveUpdateDestroy(request, pk):
    return render(request, 'templates/deal_detail.html')

def ExpenseListCreate(request):
    return render(request, 'templates/expense_list_create.html')

def ExpenseRetrieveUpdateDestroy(request, pk):
    return render(request, 'templates/expense_detail.html')

def IncomeListCreate(request):
    return render(request, 'templates/income_list_create.html')

def IncomeRetrieveUpdateDestroy(request, pk):
    return render(request, 'templates/income_detail.html')