from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    MAJOR_CHOICES = [
        "Major 1",
        "Major 2",
    ]
    #major = forms.ChoiceField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
