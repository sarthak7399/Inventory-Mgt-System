from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin

# Create your models here.

# The user model is created by inheriting from AbstractUser, which is provided by Django. It has all the necessary fields and methods for authentication.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)  # Add db_index for faster case-insensitive lookups
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)  # Consider using is_staff instead
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'  # Required for custom user models
    REQUIRED_FIELDS = ['email']  # Required fields for creating a user

    # objects = UserManager()
    def __str__(self):
        return self.full_name
    

class CounterParty(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_person = models.CharField(max_length=255)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.CharField(max_length=255)
    initial_qty = models.IntegerField()
    available_qty = models.IntegerField()

    def __str__(self):
        return self.product


class Deal(models.Model):
    DEAL_TYPES = [
        ('Sale', 'sale'),
        ('Purchase', 'purchase'),
    ]
    deal_type = models.CharField(max_length=20, choices=DEAL_TYPES)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    gross_qty = models.FloatField()
    net_qty = models.FloatField()
    counterparty = models.ForeignKey(CounterParty, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    shipment_date = models.DateTimeField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.deal_type} of {self.inventory.product} with {self.counterparty}"
    
    def handle_deal(self):
        if self.deal_type == 'Sale' or self.deal_type == 'sell':
            # Handle Sale Deal
            if self.net_qty > self.inventory.available_qty:
                raise ValueError("Insufficient inventory available for sale")
            self.inventory.available_qty -= self.net_qty
            self.inventory.save()  # Save the changes to update the available quantity
            counterparty_name = self.counterparty.name
            product_name = self.inventory.product
            Income.objects.create(deal=self, label='Sale Income', description=f'Income from selling of {product_name} with {counterparty_name}', amount=self.amount)
        elif self.deal_type == 'Purchase' or self.deal_type == 'purchase':
            # Handle Purchase Deal
            self.inventory.available_qty += self.net_qty
            self.inventory.save()  # Save the changes to update the available quantity
            counterparty_name = self.counterparty.name
            product_name = self.inventory.product
            Expense.objects.create(deal=self, label='Purchase Expense', description=f'Expense from purchase of {product_name} with {counterparty_name}', amount=self.amount)

class Expense(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()

    def __str__(self):
        return self.description
    

class Income(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()

    def __str__(self):
        return self.description