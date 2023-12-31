"""SessionsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApps1 import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('check_view/', views.check_view),

    # application-1
    path('count_view/', views.count_view),

    # application-2
    path('home_view/', views.home_view),
    path('second/', views.date_time_view),
    path('result/', views.result_view),

    # application-3
    path('name_view/', views.name_view),
    path('age_view/', views.age_view),
    path('parent_view/', views.parent_view),
    path('result1_view/', views.result1_view),

    # application-4
    path('home1/', views.index1),
    path('additem/', views.additem_view),
    path('displayitems/', views.displayitem_view),

}
