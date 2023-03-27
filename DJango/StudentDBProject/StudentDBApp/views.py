from django.shortcuts import render
from StudentDBApp.models import Student

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);

