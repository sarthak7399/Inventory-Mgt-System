from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin

# Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not username:
#             raise ValueError('Users must have a username')
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(username=username, email=email)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password):
#         user = self.create_user(username=username, email=email, password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)  # Add db_index for faster case-insensitive lookups
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)  # Consider using is_staff instead
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'  # Required for custom user models
    REQUIRED_FIELDS = ['email']  # Required fields for creating a user

    # objects = UserManager()

    def __str__(self):
        return self.username
    

# class User():
#     username = models.CharField(max_length=100, unique=True, db_index=True)  # Add db_index for faster case-insensitive lookups
#     email = models.EmailField(unique=True)
#     admin = models.BooleanField(default=False)  # Consider using is_staff instead
#     active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'username'  # Required for custom user models
#     REQUIRED_FIELDS = ['email']  # Required fields for creating a user

#     objects = UserManager()


    
class CounterParty(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_person = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

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
