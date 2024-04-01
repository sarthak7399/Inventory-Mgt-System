from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class CounterParty(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_person = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Inventory(models.Model):
    product = models.CharField(max_length=255)
    initial_qty = models.IntegerField()
    available_qty = models.IntegerField()

class Deal(models.Model):
    DEAL_TYPES = [
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
    ]
    deal_type = models.CharField(max_length=20, choices=DEAL_TYPES)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    gross_qty_mt = models.FloatField()
    net_qty_mt = models.FloatField()
    counterparty = models.ForeignKey(CounterParty, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    shipment_date = models.DateTimeField()

class Expense(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()

class Income(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.FloatField()
