from django.shortcuts import render


# Create your views here.
def wishes(request):
    return render(request, 'FirstApp/wishes.html')


def hello(request):
    return render(request, 'FirstApp/hello.html')


import datetime
import time


# {{templ-taglvars}}
def datetimefunction(request):
    date1 = datetime.datetime.now()
    print(date1)
    date2 = time.ctime()
    dict1 = {"server_datetime": date1, "server_datetime2": date2}
    return render(request, 'FirstApp/datetime.html', context=dict1)


# student data & date and time

def student_datetime(request):
    date1 = datetime.datetime.now()
    date2 = time.ctime()
    rollno = 1001
    sname = 'sai'
    marks = 95
    dict1 = {'server_datetime': date1, 'server_datetime2': date2, 'rollno': rollno, 'sname': sname, 'marks': marks}
    return render(request, 'FirstApp/studentdatetime.html', dict1)
