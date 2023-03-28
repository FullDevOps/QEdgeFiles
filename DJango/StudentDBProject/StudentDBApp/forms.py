# (write from-class)
from django import forms
class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()

class StudentLoginForm(forms.Form):
	username=forms.CharField();
	password=forms.CharField(widget=forms.PasswordInput)
