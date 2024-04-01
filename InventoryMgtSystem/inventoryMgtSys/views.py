from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def createUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to homepage after creating user

    context = {'form': form}
    return render(request, 'create_user.html', context)

def UserRetrieveUpdateDestroy(request, pk):
    return render(request, 'user_detail.html')

def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                HttpResponse('Invalid username or password')  # Display error message
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})

def CounterPartyListCreate(request):
    return render(request, 'templates/counterparty_list_create.html')

def CounterPartyRetrieveUpdateDestroy(request, pk):
    return render(request, 'templates/counterparty_detail.html')

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