from django.shortcuts import render
from django.http import HttpResponse

def f11(request):
	return HttpResponse("<h2 style='color:Blue;'>Hello, Good Morning User..!! Have a Nice day...</h2><hr/>")
