from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_per_page = 15
admin.site.register(Account, AccountAdmin)
