from django.contrib import admin
from structure.accounts.models.base import User
from structure.accounts.models.employee import Employee


# Register your models here.

admin.site.register(User)
admin.site.register(Employee)