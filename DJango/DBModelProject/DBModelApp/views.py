from django.shortcuts import render
from DBModelApp.models import Employee

#Create your views here.
def empdata(request):
    emplist=Employee.objects.all() # select * from emp table
    dict1={'emplist':emplist}
    return render(request, 'DBModelApp/emp.html', context=dict1);
