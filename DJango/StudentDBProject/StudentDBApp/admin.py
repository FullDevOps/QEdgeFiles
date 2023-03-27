from django.contrib import admin
from StudentDBApp.models import Student
#Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Student,StudentAdmin);
