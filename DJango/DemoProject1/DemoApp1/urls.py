from django.urls import path
from DemoApp1 import views

urlpatterns = [
    path('first/', views.f1),
    path('second/', views.f2),
]
