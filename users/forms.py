from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #May need to be required if we want to link it with google?

    class Meta:
        model = User #to affect this model
        fields = ['username', 'email', 'password1', 'password2']

