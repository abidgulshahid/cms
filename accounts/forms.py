from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		print (dir(model))
		fields = ('first_name','username','email','password')
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('first_name','username','email','password')
		print()
