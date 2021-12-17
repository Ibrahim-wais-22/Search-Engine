from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from searchEngine.models import Crawl_tb

class SigunpForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username','email','password1','password2']

class DishboardForm(forms.ModelForm):
    class Meta:
        model =  Crawl_tb
        fields = ['url',]

