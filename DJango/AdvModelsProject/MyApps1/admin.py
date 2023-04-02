from django.contrib import admin
from MyApps1.models import Employees


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr'];


admin.site.register(Employees, EmployeesAdmin)
