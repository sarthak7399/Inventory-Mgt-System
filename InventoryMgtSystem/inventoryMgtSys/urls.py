from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # User Endpoints
    path('users/', views.createUser, name='create-user'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy, name='user-detail'),
    path('login/', views.userLogin, name='login'),

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
