from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
        # fields = '__all__'
		fields = ('username', 'email','role','dep', 'password1', 'password2')