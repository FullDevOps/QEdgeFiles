from django.shortcuts import render
from django.http import HttpResponse

#Create our views here...
def display(request):
	ss = "<h1>Hello User, Welcome to Django First-Project(DJMyProject1) & First-App(MyApps1)</h1><hr />"
	return HttpResponse(ss)

