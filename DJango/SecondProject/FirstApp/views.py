from django.shortcuts import render

# Create your views here.
def wishes(request):
    return render(request,'FirstApp/wishes.html')

def hello(request):
    return render(request,'FirstApp/hello.html')
