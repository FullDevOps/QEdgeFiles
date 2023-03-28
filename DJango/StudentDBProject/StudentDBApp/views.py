from django.shortcuts import render
from StudentDBApp.models import Student

#Create your views here.
def studentview(request):		#old
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);


from StudentDBApp.models import Student2;
def student_homepage(request):				#new
    #students= Student2.objects.all()
    #students=Student2.objects.filter(marks__lt=35)
    #students=Student2.objects.filter(name__startswith='A')
    #students=Student2.objects.all().order_by('marks')  #ASC
    students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentDBApp/index.html', {'students':students})

#form-view(html-form)
from StudentDBApp import forms;
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentDBApp/input.html',context=dict1)

