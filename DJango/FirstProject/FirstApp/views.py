from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr /></center>";
	return HttpResponse(ss);


def show(request): 
	ss = '''<!--
	HTML Webpage to display 'Welcome-Message' with different Headings 
	(D:\temp\HTML\Welcome.html)
-->

<html>
	<head>
		<title>***Weclome-Page***</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color='brown' width='95%'/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color='brown' width='85%'/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color='brown' width='75%'/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color='brown' width='65%'/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color='brown' width='55%'/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color='brown' width='45%'/>
		</center>
	</body>
</html>
'''
	return HttpResponse(ss); 


def hello(request):
	ss = '''
	<!DOCTYPE html>
    <head>
        <titel>HEllo Webpage</titel>
        <style>
            h1{
                color:blueviolet;
            }
            h2{
                color:greenyellow;
            }
            h3{
                color:red;
            }
            h1,h2,h3{
                background-color: plum;
                width: 60%;
                width: 2px Solid Brown;
            }
        </style>
    </head>
    <body>
        <h1>Hello user...!!!</h1>
        <hr color="Brown" width="80%"/>
        <h2>Welcome to django app...</h2>
        <hr color="red" width="80%"/>
        <h3>Have a NICE Day dear ...! </h3>
        <hr color="greenyellow" width="90%"/>
	
    </body>
	
	'''
	return HttpResponse(ss)
    