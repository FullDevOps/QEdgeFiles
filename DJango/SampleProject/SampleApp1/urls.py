#SampleApp1/urls.py file

# from django.conf.urls import url;	#old
from django.urls import path;	#new
from django.urls import re_path;
from SampleApp1 import views;

urlpatterns = [ 
	path('one/', views.f11), 
	path('two/', views.f22),

    re_path('^.*$',views.homepage),  #no-url or def-url or HOME PAGE

];
