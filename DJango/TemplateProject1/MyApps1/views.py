from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request, 'MyApps1/child.html')


def f11(request):
    return render(request, 'MyApps1/child1.html')
def demo1(request):
    dict1 = {'msg1':'SaiRamKumar','msg2':'SaiRamKumar','msg3':'Hello','msg4':'SaiRamKumar','msg5':'SaiRamKumar'}
    return render(request, 'MyApps1/demo1.html', context=dict1)
