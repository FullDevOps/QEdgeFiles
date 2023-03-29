from django.shortcuts import render


# Create your views here.
def f1(request):
    return render(request, 'MyApps1/child.html')


def f11(request):
    return render(request, 'MyApps1/child1.html')


def demo1(request):
    dict1 = {'msg1': 'SaiRamKumar', 'msg2': 'SaiRamKumar', 'msg3': 'Hello', 'msg4': 'SaiRamKumar',
             'msg5': 'SaiRamKumar'}
    return render(request, 'MyApps1/demo1.html', context=dict1)


import datetime

def demo2(request):
    date1 = datetime.datetime.now()
    dict1 = {'name': 'SaiRamKumar', 'subject': 'CSEEngg', 'dept': 'CSEDept', 'date1': date1}
    return render(request, 'MyApps1/demo2.html', context=dict1)
def demo3(request):
    return render(request,'MyApps1/demo3.html');

def thankyou(request):
    return render(request,'MyApps1/thankyou.html');
