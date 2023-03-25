from django.shortcuts import render

# Create your views here.
def wishes(request):
    return render(request,'FirstApp/wishes.html')

def hello(request):
    return render(request,'FirstApp/hello.html')

import datetime
import time


#{{templ-taglvars}}
def datetimefunction(request):
    date1 = datetime.datetime.now()
    print(date1)
    date2 = time.ctime()
    dict1={"server_datetime":date1,"server_datetime2":date2}
    return render(request,'FirstApp/datetime.html',context=dict1)