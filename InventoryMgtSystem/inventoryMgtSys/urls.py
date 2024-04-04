from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # User Endpoints
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # CounterParty Endpoints
    path('counterparty/', views.counterparty_list, name='counterparty_list'),
    path('counterparty/add/', views.counterparty_add, name='counterparty_add'),
    path('counterparty/edit/<int:pk>/', views.counterparty_edit, name='counterparty_edit'),
    path('counterparty/delete/<int:pk>/', views.counterparty_delete, name='counterparty_delete'),

    # Inventory Endpoints
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),
    path('inventory/edit/<int:pk>/', views.inventory_edit, name='inventory_edit'),
    path('inventory/delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),

    # Deal Endpoints
    path('deals/', views.deal_list, name='deal_list'),
    path('deals/add/', views.deal_add, name='deal_add'),
    path('deals/edit/<int:pk>/', views.deal_edit, name='deal_edit'),
    path('deals/delete/<int:pk>/', views.deal_delete, name='deal_delete'),

    # Expense Endpoints
    path('expense/', views.expense_list, name='expense_list'),
    path('expense/add/', views.expense_add, name='expense_add'),
    path('expense/edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('expense/delete/<int:pk>/', views.expense_delete, name='expense_delete'),

    # Income Endpoints
    path('income/', views.income_list, name='income_list'),
    path('income/add/', views.income_add, name='income_add'),
    path('income/edit/<int:pk>/', views.income_edit, name='income_edit'),
    path('income/delete/<int:pk>/', views.income_delete, name='income_delete'),

    path('contactus', views.contactus, name='contactus'),
    path('features', views.features, name='features'),
]
