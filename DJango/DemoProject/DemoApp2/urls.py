# from django.conf.urls import url;	#old
from django.urls import path;	#new
from django.urls import re_path;

from DemoApp2 import views;

urlpatterns = [ 
	path('third/', views.f3), 
	path('fourth/', views.f4),
];
