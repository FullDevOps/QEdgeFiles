from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr /></center>";
	return HttpResponse(ss);