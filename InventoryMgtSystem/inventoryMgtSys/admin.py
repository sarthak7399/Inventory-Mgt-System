from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(User) # We should not use this to register the user model because in settings.py we have set AUTH_USER_MODEL = 'inventoryMgtSys.User'

admin.site.register(CounterParty)
admin.site.register(Inventory)
admin.site.register(Deal)
admin.site.register(Expense)
admin.site.register(Income)

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'admin', 'active')
#     search_fields = ('username', 'email')
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(User, CustomUserAdmin)

