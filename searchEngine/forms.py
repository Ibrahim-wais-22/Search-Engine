from django import forms
from .models import Crawl_tb ,AddCommint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SigunpForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username','email',]

class AddForm(forms.ModelForm):
    class Meta:
        model =  AddCommint
        fields = '__all__'





