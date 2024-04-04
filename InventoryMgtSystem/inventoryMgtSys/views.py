from pyexpat.errors import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
                return redirect('counterparty_list')  # Redirect to Counterparties listing
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


def counterparty_list(request):
   counterparties = CounterParty.objects.all()
   return render(request, 'counterparty.html', {'counterparties': counterparties})

def counterparty_add(request):
   if request.method == 'POST':
       form = CounterPartyForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('counterparty_list')
   else:
       form = CounterPartyForm()
   return render(request, 'counterparty_form.html', {'form': form})

def counterparty_edit(request, pk):
   counterparty = get_object_or_404(CounterParty, pk=pk)
   if request.method == 'POST':
       form = CounterPartyForm(request.POST, instance=counterparty)
       if form.is_valid():
           form.save()
           return redirect('counterparty_list')
   else:
       form = CounterPartyForm(instance=counterparty)
   return render(request, 'counterparty_form.html', {'form': form})

def counterparty_delete(request, pk):
   counterparty = get_object_or_404(CounterParty, pk=pk)
   if request.method == 'POST':
       counterparty.delete()
       return redirect('counterparty_list')
   return render(request, 'counterparty_confirm_delete.html', {'counterparty': counterparty})



def inventory_list(request):
   inventories = Inventory.objects.all()
   return render(request, 'inventory.html', {'inventories': inventories})

def inventory_add(request):
   if request.method == 'POST':
       form = InventoryForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('inventory_list')
   else:
       form = InventoryForm()
   return render(request, 'inventory_form.html', {'form': form})

def inventory_edit(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   if request.method == 'POST':
       form = InventoryForm(request.POST, instance=inventory)
       if form.is_valid():
           form.save()
           return redirect('inventory_list')
   else:
       form = InventoryForm(instance=inventory)
   return render(request, 'inventory_form.html', {'form': form})

def inventory_delete(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   if request.method == 'POST':
       inventory.delete()
       return redirect('inventory_list')
   return render(request, 'inventory_confirm_delete.html', {'inventory': inventory})



def deal_list(request):
    deals = Deal.objects.all()
    return render(request, 'deal.html', {'deals': deals})

def deal_add(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save()
            deal.handle_deal()  # Call handle_deal method
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request, 'deal_form.html', {'form': form})

def deal_edit(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm(instance=deal)
    return render(request, 'deal_form.html', {'form': form})

def deal_delete(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        deal.delete()
        return redirect('deal_list')
    return render(request, 'deal_confirm_delete.html', {'deal': deal})



def expense_list(request):
   expenses = Expense.objects.all()
   return render(request, 'expense.html', {'expenses': expenses})

def expense_add(request):
   if request.method == 'POST':
       form = ExpenseForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('expense_list')
   else:
       form = ExpenseForm()
   return render(request, 'expense_form.html', {'form': form})

def expense_edit(request, pk):
   expense = get_object_or_404(Expense, pk=pk)
   if request.method == 'POST':
       form = ExpenseForm(request.POST, instance=expense)
       if form.is_valid():
           form.save()
           return redirect('expense_list')
   else:
       form = ExpenseForm(instance=expense)
   return render(request, 'expense_form.html', {'form': form})

def expense_delete(request, pk):
   expense = get_object_or_404(Expense, pk=pk)
   if request.method == 'POST':
       expense.delete()
       return redirect('expense_list')
   return render(request, 'expense_confirm_delete.html', {'expense': expense})



def income_list(request):
   incomes = Income.objects.all()
   return render(request, 'income.html', {'incomes': incomes})

def income_add(request):
   if request.method == 'POST':
       form = IncomeForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('income_list')
   else:
       form = IncomeForm()
   return render(request, 'income_form.html', {'form': form})

def income_edit(request, pk):
   income = get_object_or_404(Income, pk=pk)
   if request.method == 'POST':
       form = IncomeForm(request.POST, instance=income)
       if form.is_valid():
           form.save()
           return redirect('income_list')
   else:
       form = IncomeForm(instance=income)
   return render(request, 'income_form.html', {'form': form})

def income_delete(request, pk):
   income = get_object_or_404(Income, pk=pk)
   if request.method == 'POST':
       income.delete()
       return redirect('income_list')
   return render(request, 'income_confirm_delete.html', {'income': income})


def contactus(request):
    return render(request, 'contactus.html')

def features(request):
    return render(request, 'features.html')