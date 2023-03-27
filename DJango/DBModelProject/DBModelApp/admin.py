from django.contrib import admin
from DBModelApp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr'];

admin.site.register(Employee,EmployeeAdmin);

from DBModelApp.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['compid', 'compname', 'noofemps', 'compaddr', 'compsharevalue']

admin.site.register(Company,CompanyAdmin)