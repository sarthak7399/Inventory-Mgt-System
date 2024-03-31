# from django.db import models

# # Create your models here.

# class User(models.Model):
#     uid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     admin = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)

#     def __str__(self):  # Used for str representation
#         return self.username