# from django.conf.urls import url;	#old
from django.urls import path;	#new
from django.urls import re_path;
from DemoApp1 import views;

urlpatterns = [ 
	path('first/', views.f1), 
	path('second/', views.f2),
];

