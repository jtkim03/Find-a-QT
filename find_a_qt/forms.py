from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from .models import Student, Tutor
from phonenumber_field.modelfields import PhoneNumberField


class StudentRegistration(ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'year_in_school', 'major', 'phone_number')
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter First and Last Names', 'aria-label' : 'Student', 'aria-describedby' : 'add-btn'}
            ),
            'major': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Major',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            )

        }


class TutorRegistrationForm(ModelForm):

    class Meta:
        model = Tutor
        fields = ('name', 'year_in_school', 'major', 'phone_number')
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Enter First and Last Names', 'aria-label' : 'Student', 'aria-describedby' : 'add-btn'}
            ),
            'major': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Major',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            ),
            'phone_number': forms.TextInput(
                attrs={'class' : 'form-control',
                       'placeholder' : 'Enter Phone Number',
                       'aria-label' : 'Student',
                       'aria-describedby' : 'add-btn'}
            )
        }
