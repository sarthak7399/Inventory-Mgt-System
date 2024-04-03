from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dash, name='dashboard'),

    # User Endpoints
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy, name='user-detail'),

    # CounterParty Endpoints
    path('counterparties/', views.CounterPartyListCreate, name='counterparty-list-create'),
    path('counterparties/<int:pk>/', views.CounterPartyRetrieveUpdateDestroy, name='counterparty-detail'),

    # Inventory Endpoints
    path('inventories/', views.InventoryListCreate, name='inventory-list-create'),
    path('inventories/<int:pk>/', views.InventoryRetrieveUpdateDestroy, name='inventory-detail'),

    # Deal Endpoints
    path('deals/', views.DealListCreate, name='deal-list-create'),
    path('deals/<int:pk>/', views.DealRetrieveUpdateDestroy, name='deal-detail'),

    # Expense Endpoints
    path('expenses/', views.ExpenseListCreate, name='expense-list-create'),
    path('expenses/<int:pk>/', views.ExpenseRetrieveUpdateDestroy, name='expense-detail'),

    # Income Endpoints
    path('incomes/', views.IncomeListCreate, name='income-list-create'),
    path('incomes/<int:pk>/', views.IncomeRetrieveUpdateDestroy, name='income-detail'),
]
