from django import forms


class LoginForm(forms.Form):
    name = forms.CharField()


class ItemAddForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
